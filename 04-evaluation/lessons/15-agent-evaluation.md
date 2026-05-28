# Agent Evaluation

For RAG, we saved the final answer and compared it with the original
FAQ answer.

For agents, we do the same thing, but we also save the tool calls. The
tool calls show the trajectory: what the agent decided to do before it
produced the final answer.

We'll keep this simple and reuse the agent from module 01.

For each question, we capture:

- the user question
- the final answer
- the tool calls made by the agent

Then we can check if the answer is good and look at whether the
trajectory makes sense.

## Capturing tool calls

Use the same `search` function and `search_tool` schema from the
agentic RAG lesson.

The only change is that we keep a list of tool calls while the agent
runs:

```python
import json

def make_call(call):
    args = json.loads(call.arguments)
    result = search(**args)
    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }
```

Now run the agent.

Store the answer and the trajectory:

```python
def agent_with_logging(question, model="gpt-5.4-mini"):
    messages = [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": question}
    ]
    tool_calls = []
    answer = None

    while True:
        response = openai_client.responses.create(
            model=model,
            input=messages,
            tools=[search_tool],
        )
        messages.extend(response.output)
        has_tool_calls = False

        for entry in response.output:
            if entry.type == "message":
                answer = entry.content[0].text

            if entry.type == "function_call":
                tool_calls.append({
                    "name": entry.name,
                    "arguments": entry.arguments,
                })

                result = make_call(entry)
                messages.append(result)
                has_tool_calls = True

        if not has_tool_calls:
            break

    return {
        "answer": answer,
        "tool_calls": tool_calls,
    }
```

The `answer` is what we evaluate the same way as before. The
`tool_calls` list lets us see how the agent got there.

## Trying one question

Run the agent for one ground truth question:

```python
rec = ground_truth[0]
agent_result = agent_with_logging(rec["question"])

agent_result
```

Print the trajectory:

```python
for call in agent_result["tool_calls"]:
    print(call["name"], call["arguments"])
```

This is the extra signal we get from an agent. If the answer is wrong,
the trajectory can help explain why. Maybe the agent searched for the
wrong thing, repeated the same query, or stopped too early.

## Processing multiple questions

Run the agent for a small sample:

```python
from tqdm.auto import tqdm

agent_results = []

for rec in tqdm(ground_truth[:50]):
    result = agent_with_logging(rec["question"])
    result["document"] = rec["document"]
    agent_results.append(result)
```

Turn it into a dataframe:

```python
import pandas as pd

df_agent = pd.DataFrame(agent_results)
```

Add a simple tool-call count:

```python
tool_call_counts = []

for calls in df_agent["tool_calls"]:
    tool_call_counts.append(len(calls))

df_agent["num_tool_calls"] = tool_call_counts
```

Check the distribution:

```python
df_agent["num_tool_calls"].describe()
```

Look at examples with many tool calls:

```python
df_agent.sort_values("num_tool_calls", ascending=False).head()
```

This is enough for a first pass. We can evaluate the final answer with
the same LLM-as-a-judge approach as in the previous lesson. Then we use
the trajectory to understand how the agent behaved.

[← LLM as a Judge](14-llm-as-judge.md) | [Next Steps →](16-next-steps.md)
