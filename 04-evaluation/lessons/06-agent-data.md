# Collecting Agent Data

In module 03, we built agents that use tools to answer questions. The
agent loop runs the LLM, checks for function calls, executes them, and
repeats until the LLM gives a final answer.

Evaluating agents is more complex than evaluating RAG. Not only do we
need to check if the answer is correct, but also:

- Is the agent using tools efficiently?
- Is it making unnecessary or duplicate tool calls?
- Is it following the instructions in the developer prompt?

Before we can evaluate any of this, we need to collect data. For each
query, we record:

- The question
- The sequence of tool calls (the trajectory)
- The final answer

In this lesson, we set up the agent with logging and collect data from
our ground truth questions.


## Setting up the agent

Let's set up the agent from module 03. The search function, search tool
schema, and developer prompt are the same:

```python
from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

def search(query, course="data-engineering-zoomcamp"):
    boost_dict = {"question": 3.0, "section": 0.5}
    results = index.search(
        query,
        boost_dict=boost_dict,
        filter_dict={"course": course},
        num_results=5
    )
    return results
```

```python
import json

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

developer_prompt = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function.
Use as many keywords from the user question as possible when making first requests.

Make multiple searches if needed. Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()

def make_call(call):
    args = json.loads(call.arguments)
    f_name = call.name
    f = globals()[f_name]
    result = f(**args)
    result_json = json.dumps(result, indent=2)
    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }
```


## Running the agent with logging

We modify the agent loop to collect the tool call trajectory:

```python
def agent_with_logging(question, model="gpt-5.4-mini"):
    chat_messages = [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": question}
    ]

    tools = []
    answer = None

    while True:
        response = openai_client.responses.create(
            model=model,
            input=chat_messages,
            tools=[search_tool],
        )

        chat_messages.extend(response.output)
        has_function_calls = False

        for entry in response.output:
            if entry.type == "message":
                answer = entry.content[0].text
            if entry.type == "function_call":
                tools.append({
                    "name": entry.name,
                    "args": entry.arguments
                })
                result = make_call(entry)
                chat_messages.append(result)
                has_function_calls = True

        if not has_function_calls:
            break

    return {
        "question": question,
        "tools": tools,
        "answer": answer,
    }
```

The `tools` list records every function call the agent makes. This is
the trajectory -- the sequence of actions the agent took to answer the
question.


## Collecting results

Let's run the agent on ground truth questions and collect the data:

```python
from tqdm.auto import tqdm

doc_idx = {d['id']: d for d in documents}
agent_results = {}

for i, rec in enumerate(tqdm(ground_truth_flat[:50])):
    result = agent_with_logging(rec['question'])
    result['document'] = rec['document']
    result['course'] = rec['course']
    agent_results[i] = result
```

Let's look at a result:

```python
r = agent_results[0]
print("Question:", r['question'])
print("Tool calls:", len(r['tools']))
for t in r['tools']:
    print(f"  {t['name']}({t['args']})")
print("Answer:", r['answer'][:100], "...")
```

Now we have the data we need. In the next two lessons, we'll evaluate
the agent on three dimensions:

1. Answer correctness (did it give the right answer?)
2. Trajectory efficiency (did it use tools well?)
3. Instruction following (did it follow the developer prompt rules?)

[<- LLM as a Judge](05-llm-as-judge.md) | [Trajectory Evaluation ->](07-trajectory-evaluation.md)
