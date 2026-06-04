# Function Calling

Video: [Watch this lesson](https://www.youtube.com/watch?v=CeEki_0mdGo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous lesson we built a RAG pipeline with `RAGBase.rag()`
and saw it fail on the "Olama" typo. The search returned nothing
useful, and the LLM had no way to recover.

The flow that broke:

```mermaid
flowchart TD
    U([User: How do I run Olama?])
    S[search - Olama - no useful results]
    A([LLM: I don't have information about Olama.])

    U --> S --> A
```

The pipeline is fixed: search, build prompt, LLM.

```python
def rag(self, query):
    search_results = self.search(query)
    prompt = self.build_prompt(query, search_results)
    answer = self.llm(prompt)
    return answer
```

The LLM is a passenger here, not a driver. It never sees the bad
search results, so it can't try again with a corrected query.

## The agent alternative

An agent puts the LLM in charge.

Instead of running search ourselves, we give the LLM a `search` tool.
It decides when to call it and what to search for.

The same typo question now goes like this:

```mermaid
flowchart TD
    U([User: How do I run Olama?])
    L1[LLM: I'll search for 'Olama']
    S1[search - Olama - no useful results]
    L2[LLM: Hmm, no results. Maybe a typo for 'Ollama'?]
    S2[search - Ollama - found results!]
    A([LLM: Here's how to run Ollama locally...])

    U --> L1 --> S1 --> L2 --> S2 --> A
```

The LLM searched, saw the results were bad, and decided to try again
with a different query. It made that decision on its own. We didn't
write any code to handle typos.

The difference is about who makes the decisions:

- With RAG, the developer decides. We fix the steps up front, so
  search always runs once with the exact user query.
- With an agent, the LLM decides. It chooses which actions to take
  and when to stop.

The mechanism that makes this possible is function calling, and that's
what the rest of this lesson is about.

## Asking without tools

First, let's see what the LLM does without any tools. We ask it a
course-specific question and look at the answer.

```python
messages = [
    {"role": "user", "content": "I just discovered the course. Can I join it?"}
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
)

response.output_text
```

The model answers from its general knowledge, something like "it
depends on the course" or "check the course website". It doesn't know
about our FAQ, so the answer is vague and not helpful. This is exactly
why we need RAG, and why we want to hand the model a tool.

## Defining the tool

First we define a top-level `search` function that queries the `index`
directly. The model will reference it by this name. We keep the Python
function and the tool name aligned so the dispatch is easier later.

```python
def search(query):
    boost_dict = {"question": 3.0, "section": 0.5}
    filter_dict = {"course": "llm-zoomcamp"}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
        filter_dict=filter_dict
    )
```

Next we tell the model about this function. The model doesn't see our
Python code, only a schema describing what the function does and what
arguments it takes. LLMs are language agnostic. At the end we're just
making an HTTP call, so we describe the tool in JSON rather than in
Python. The same schema would work from TypeScript or Java.

```python
search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the FAQ database for entries matching the given query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text to look up in the course FAQ."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}
```

The `description` is the most important field, because the model reads
it to decide when to call the function. `parameters` is a JSON schema
for the arguments, and we mark `query` as required so the model always
fills it in.

## Sending the question with the tool

Now we send the same question as before, but this time we include the
tool in the request:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=[search_tool],
)

response.output
```

Look at the output. Instead of a message with the answer, the response
contains a `function_call` entry. The model decided it needs to search
the FAQ before answering. Rather than reply, it asked us to run the
search function first.

Look at the arguments too. The model didn't pass our question
verbatim. It judged the raw question wasn't the best query to search
with. So it rewrote our enrollment question into search keywords like
"enroll late join course".

## Executing the function and sending the result back

The function call contains JSON arguments. We parse them, call our
`search` function, and serialize the result.

```python
import json

call = response.output[0]
args = json.loads(call.arguments)

results = search(**args)
result_json = json.dumps(results, indent=2)
```

Now we send this result back to the model. First, we add the model's
output to the conversation history - the model needs to see its own
function call. Then we add the tool result.

```python
messages.extend(response.output)

messages.append({
    "type": "function_call_output",
    "call_id": call.call_id,
    "output": result_json,
})
```

The `call_id` links the tool result to the specific function call the
model requested. If the model makes multiple function calls in one
turn, each one gets its own `call_id`.

## Asking the model again

We call the API a second time with the expanded history:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=[search_tool],
)

response.output_text
```

This time the model has the original question, its own decision to
call `search`, and the FAQ results. It can now produce a proper
course-specific answer.

We have to send the whole history because LLMs are stateless between
API calls. The memory is the list you send as `input`. If you send
only the tool result, the model has no idea what's going on. So on
this second call we replay everything we have so far. That means the
question, the decision to call `search`, and the result we got back.

That's the full function-calling loop for a single turn. With plain
RAG we made one call, and here we make two. Turning RAG agentic means
more round-trips.

People call this pattern "agentic RAG", "tool use", or "function
calling". The idea behind all of them is the same. The LLM decides
which tools to call.

## Token usage and cost

We just made two API calls instead of one. Each call we send to the
model costs money, so it's worth checking how much one tool-using turn
actually costs.

The response has a `usage` field with the token counts:

```python
usage = response.usage
usage.input_tokens, usage.output_tokens
```

For each model the provider publishes a price per million input tokens
and per million output tokens. Plug those numbers in to convert tokens
to dollars.

```python
def calculate_gpt54mini_price(input_tokens, output_tokens):
    INPUT_PRICE_PER_MILLION = 0.15
    OUTPUT_PRICE_PER_MILLION = 0.60

    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION
    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost,
    }

result = calculate_gpt54mini_price(652, 33)
print("Total cost: $", round(result["total_cost"], 8))
```

This usage is only for the second API call. The first call also has
its own usage and its own cost. That was the call where the model
decided to invoke `search`. Two calls means we pay twice. We pay even
more on the second call, because we resend the full history as input.

With a real agent loop the model can make many calls, so the costs add
up. Keep an eye on `usage` while you develop.

[← Quick RAG Revision](12-rag-revision.md) | [The Agentic Loop →](14-agentic-loop.md)
