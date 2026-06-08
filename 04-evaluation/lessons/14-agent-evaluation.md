# Agent Evaluation

Video: [Watch this lesson](https://www.youtube.com/watch?v=2SW86BehVdI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

For RAG, we used the A->Q->A' setup:

- A = original answer in the FAQ
- Q = generated question from this answer
- A' = answer produced by our RAG system

For agents, we use the same setup. A' comes from an agent instead of a
fixed RAG pipeline.

We also save the trajectory. Here, the trajectory means only the tool
calls the agent made before producing the final answer.

## Loading the data

Use the same ground truth questions:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground_truth-new.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Load the FAQ documents and the search index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()

documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

documents = documents_llm
index = build_index(documents)
```

Create a lookup table:

```python
doc_idx = {}

for doc in documents:
    doc_idx[doc["id"]] = doc
```

## Running the agent

Reuse the ToyAIKit agent from module 01. It handles the agent loop and
stores the full message history.

First, set up the model clients:

```python
from dotenv import load_dotenv
from openai import OpenAI
from toyaikit.llm import OpenAIClient

load_dotenv()
openai_client = OpenAI()
```

Define the search tool:

```python
def search(query: str) -> list[dict]:
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={"question": 1.0, "answer": 2.0, "section": 0.1},
        filter_dict={"course": "llm-zoomcamp"}
    )
```

Create the runner:

```python
from toyaikit.tools import Tools
from toyaikit.chat.runners import OpenAIResponsesRunner

agent_tools = Tools()
agent_tools.add_tool(search)

instructions = """
You're a course teaching assistant. Answer student questions based on
the FAQ search results. Use the search tool before answering.
""".strip()

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=instructions,
    llm_client=OpenAIClient(model="gpt-5.4-mini")
)
```

The result contains:

- `last_message`: the final response
- `all_messages`: the full message history
- `cost`: the cost of all LLM calls in this run

Run it for one ground truth question:

```python
rec = ground_truth[0]

result = runner.loop(prompt=rec["question"])
```

Look at the full message history:

```python
result.all_messages
```

For this lesson, the trajectory is only the tool calls. We don't need
to send the full message history to the judge.

Extract the function name and arguments:

```python
def extract_tool_calls(messages):
    tool_calls = []

    for message in messages:
        if isinstance(message, dict):
            continue

        if message.type == "function_call":
            tool_calls.append({
                "name": message.name,
                "arguments": message.arguments,
            })

    return tool_calls
```

For this example:

```python
tool_calls = extract_tool_calls(result.all_messages)

tool_calls
```

You should see something like this:

```python
[
    {
        "name": "search",
        "arguments": "{\"query\":\"own pace certificate at the end self-paced course certificate\"}"
    }
]
```

Get the original answer:

```python
doc_id = rec["document"]
original_doc = doc_idx[doc_id]
answer_orig = original_doc["answer"]
```

Save the A->Q->A' record and the trajectory:

```python
agent_result = {
    "question": rec["question"],
    "answer_agent": result.last_message,
    "answer_orig": answer_orig,
    "tool_calls": tool_calls,
    "cost": result.cost.total_cost,
    "document": doc_id,
}

agent_result
```

The `answer_agent` field is what we evaluate with the LLM judge. The
`tool_calls` field lets the judge see how the agent got there.

## Processing multiple questions

Create a function that processes one ground truth record:

```python
def generate_agent_answer(rec):
    doc_id = rec["document"]
    original_doc = doc_idx[doc_id]

    result = runner.loop(prompt=rec["question"])

    tool_calls = extract_tool_calls(result.all_messages)

    answer_record = {
        "question": rec["question"],
        "answer_agent": result.last_message,
        "answer_orig": original_doc["answer"],
        "tool_calls": tool_calls,
        "cost": result.cost.total_cost,
        "document": doc_id,
    }

    return answer_record
```

Run it for a small sample in parallel:

```python
from concurrent.futures import ThreadPoolExecutor
from evaluation_utils import map_progress

with ThreadPoolExecutor(max_workers=6) as pool:
    agent_answers = map_progress(pool, ground_truth[:50], generate_agent_answer)
```

Turn it into a dataframe:

```python
df_agent = pd.DataFrame(agent_answers)
```

Calculate the total cost:

```python
df_agent["cost"].sum()
```

Save the results:

```python
df_agent.to_csv("data/agent-answers.csv", index=False)
```

Now we have the same A->Q->A' data as before, plus the tool calls for
each agent run.

We generated this file for the course materials on May 29, 2026. The
run used 50 ground truth questions. ToyAIKit tracks the agent cost for
each run, so we can sum the `cost` column directly.

The total agent cost was $0.06993300, about 7 cents.

If you don't want to run the agent yourself, download the file we
prepared:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget -O data/agent-answers.csv ${PREFIX}/04-evaluation/data/agent-answers.csv
```

Then load it:

```python
df_agent = pd.read_csv("data/agent-answers.csv")
agent_answers = df_agent.to_dict(orient="records")
```

Our judge can look at both:

- whether `answer_agent` matches `answer_orig`
- whether the tool calls look reasonable for the question

This lets us evaluate the final answer and the agent behavior in one
place.

## Judging answers and trajectories

A good trajectory is not just "many tool calls". A good trajectory uses
the available tools in a way that helps answer the question.

For our search agent, a good trajectory has these properties:

- The search query is relevant to the user question
- The query includes the important keywords from the question
- The agent avoids duplicate searches with the same arguments
- If it searches more than once, the next query is a useful refinement
- It usually uses 1 search call
- 2-3 calls can be okay for harder questions
- More than 3 search calls needs a clear reason
- The tool calls support the final answer
- The agent does not stop too early or keep searching without a reason

Now define a judge output type with two scores:

```python
from pydantic import BaseModel, Field
from typing import Literal

class AgentEvaluation(BaseModel):
    answer_reasoning: str = Field(
        description="Reasoning about whether the final answer is correct."
    )
    answer_score: Literal["good", "bad"] = Field(
        description="'good' if the final answer matches the original answer."
    )
    trajectory_reasoning: str = Field(
        description="Reasoning about whether the tool calls were useful."
    )
    trajectory_score: Literal["good", "bad"] = Field(
        description="'good' if the tool calls were reasonable for the question."
    )
```

The judge instructions:

```python
agent_judge_instructions = """
You are an expert evaluator. You will be given:
1. A question from a student
2. The original answer from the FAQ (ground truth)
3. An answer generated by an AI agent
4. The tool calls made by the agent

Evaluate two things:

Answer quality:
- Does the agent answer match the original answer?
- It does not need to be word-for-word identical.
- It should contain the same key information.

Trajectory quality:
- Were the search queries relevant to the question?
- Did the queries include important keywords from the question?
- Did the agent avoid duplicate or unnecessary tool calls?
- If it made multiple searches, did the later searches refine the query?
- Was the number of search calls reasonable? Usually 1 is enough, 2-3
  can be okay, and more than 3 needs a clear reason.
- Did the tool calls support the final answer?

Mark answer_score as 'good' if the final answer is correct.
Mark trajectory_score as 'good' if the tool calls were reasonable.
""".strip()

agent_judge_prompt = """
Question:
{question}

Original Answer (ground truth):
{answer_orig}

Agent Answer:
{answer_agent}

Tool Calls:
{tool_calls}
""".strip()
```

Define the judge function:

```python
import json
from evaluation_utils import calc_total_price, llm_structured_retry

def evaluate_agent_answer(rec, model="gpt-5.4-mini"):
    tool_calls = rec["tool_calls"]

    if isinstance(tool_calls, str):
        tool_calls = json.loads(tool_calls)

    prompt = agent_judge_prompt.format(
        question=rec["question"],
        answer_orig=rec["answer_orig"],
        answer_agent=rec["answer_agent"],
        tool_calls=json.dumps(tool_calls, indent=2),
    )

    result, usage = llm_structured_retry(
        openai_client,
        agent_judge_instructions,
        prompt,
        AgentEvaluation,
        model=model,
    )

    return result, usage
```

Test it on one agent result:

```python
agent_eval, usage = evaluate_agent_answer(agent_answers[0])

agent_eval
```

When the answer is bad, the trajectory score tells us whether the
problem started with tool use. If the answer is bad but the trajectory
is good, the model may have used the retrieved context poorly.
If both are bad, the agent likely searched for the wrong thing. It may
also have stopped too early.

## Running the agent judge

Run the judge for all agent answers:

```python
def judge_agent_record(rec):
    agent_eval, usage = evaluate_agent_answer(rec)

    result = {
        "question": rec["question"],
        "document": rec["document"],
        "answer_score": agent_eval.answer_score,
        "answer_reasoning": agent_eval.answer_reasoning,
        "trajectory_score": agent_eval.trajectory_score,
        "trajectory_reasoning": agent_eval.trajectory_reasoning,
    }

    return result, usage
```

Use the same parallel helper:

```python
with ThreadPoolExecutor(max_workers=6) as pool:
    results = map_progress(pool, agent_answers, judge_agent_record)
```

Split the results:

```python
agent_evaluations = []
usages = []

for evaluation, usage in results:
    agent_evaluations.append(evaluation)
    usages.append(usage)
```

Create a dataframe:

```python
df_agent_eval = pd.DataFrame(agent_evaluations)
```

Calculate the judge cost from the token usage:

```python
calc_total_price(usages)
```

Check the answer scores:

```python
df_agent_eval["answer_score"].value_counts()
```

Check the trajectory scores:

```python
df_agent_eval["trajectory_score"].value_counts()
```

Save the judge results:

```python
df_agent_eval.to_csv("data/agent-evaluations.csv", index=False)
```

We generated this file for the course materials on May 29, 2026. The
run judged 50 agent answers.

The answer scores were:

- Good: 45
- Bad: 5

The trajectory scores were:

- Good: 49
- Bad: 1

The judge token usage was:

- Input tokens: 29,228
- Output tokens: 6,984
- Cost with the prices above: $0.053349, about 5 cents

If you don't want to run the judge yourself, download the file we
prepared:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget -O data/agent-evaluations.csv ${PREFIX}/04-evaluation/data/agent-evaluations.csv
```

[← LLM as a Judge](13-llm-as-judge.md) | [Next Steps →](15-next-steps.md)
