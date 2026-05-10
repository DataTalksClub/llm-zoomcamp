# Trajectory Evaluation

In the previous lesson, we collected agent data -- for each question,
we have the tool call trajectory and the final answer. Now let's
evaluate how efficiently the agent used its tools.

A trajectory is the sequence of tool calls the agent made. For example:

```
1. search({"query": "docker windows install"})
2. search({"query": "docker desktop windows setup"})
```

This is a good trajectory: two relevant searches with different
keywords. Compare with a bad trajectory:

```
1. search({"query": "docker"})
2. search({"query": "docker"})
3. search({"query": "docker"})
```

Three duplicate calls that don't expand the search.


## What makes a good trajectory?

A good trajectory has:

- Relevant search queries that relate to the question
- No duplicate calls (same query repeated)
- A reasonable number of total calls (not excessive)
- Queries that build on previous results

A bad trajectory has:

- Duplicate tool calls (same arguments repeated)
- Completely irrelevant queries
- Excessive tool use (more than 5-6 calls for a simple question)

We can check some of these with simple code, and for the rest we use
an LLM judge.


## Simple checks

Let's start with checks we can do without an LLM:

```python
def analyze_trajectory_simple(tools):
    num_calls = len(tools)

    queries = [t['args'] for t in tools]
    unique_queries = set(queries)
    num_duplicates = num_calls - len(unique_queries)

    return {
        'num_calls': num_calls,
        'num_duplicates': num_duplicates,
        'has_duplicates': num_duplicates > 0,
    }
```

```python
for i, result in agent_results.items():
    analysis = analyze_trajectory_simple(result['tools'])
    result['num_calls'] = analysis['num_calls']
    result['has_duplicates'] = analysis['has_duplicates']

    print(f"[{i}] calls={analysis['num_calls']}, "
          f"duplicates={analysis['num_duplicates']}")
```

Simple metrics like call count and duplicate detection are fast and
free. They catch obvious problems. But they can't tell if the queries
are relevant or well-formulated.


## LLM-based trajectory evaluation

For a deeper evaluation, we ask an LLM to judge the trajectory. We
define the output format:

```python
from pydantic import BaseModel, Field
from typing import Literal

class TrajectoryResult(BaseModel):
    reasoning: str = Field(
        description="Step-by-step reasoning about the tool call trajectory."
    )
    score: Literal["good", "bad"] = Field(
        description="'good' if the trajectory was efficient, 'bad' if clearly wasteful."
    )
    suggestion: str = Field(
        description="How the agent could be more efficient, or 'none' if optimal."
    )
```

The judge instructions tell the LLM what to look for:

```python
trajectory_instructions = """
You are an expert evaluator. You will be given:
1. A user question
2. The sequence of tool calls the agent made (the "trajectory")
3. The agent's final answer

The agent has one tool: search(query) -- searches the FAQ.

Evaluate the trajectory:
- Were the search queries relevant to the question?
- Were there DUPLICATE tool calls? (same query repeated)
- Were there clearly irrelevant searches?
- More than 5 search calls is usually excessive for simple questions.

Mark "good" if the trajectory was reasonably efficient.
Mark "bad" only if there are clear inefficiencies: duplicate calls,
completely irrelevant queries, or excessive tool use.
""".strip()

trajectory_prompt = """
User Question:
{question}

Tool Call Trajectory:
{tools}

Agent's Final Answer:
{answer}
""".strip()
```

The evaluation function:

```python
def evaluate_trajectory(question, tools, answer, model="gpt-5.4-mini"):
    tools_str = "\n".join(
        f"{i+1}. {t['name']}({t['args']})"
        for i, t in enumerate(tools)
    ) or "(no tool calls)"

    prompt = trajectory_prompt.format(
        question=question,
        tools=tools_str,
        answer=answer
    )

    messages = [
        {"role": "developer", "content": trajectory_instructions},
        {"role": "user", "content": prompt}
    ]

    response = openai_client.responses.parse(
        model=model,
        input=messages,
        text_format=TrajectoryResult
    )

    return response.output_parsed
```

Now evaluate all trajectories:

```python
for i, result in agent_results.items():
    traj_eval = evaluate_trajectory(
        question=result['question'],
        tools=result['tools'],
        answer=result['answer']
    )

    result['trajectory'] = traj_eval.score
    result['trajectory_reasoning'] = traj_eval.reasoning
    result['trajectory_suggestion'] = traj_eval.suggestion
```

Check the results:

```python
import pandas as pd

df_agent = pd.DataFrame(agent_results.values())

print("Trajectory scores:")
print(df_agent['trajectory'].value_counts())
print()
print("Bad trajectories:")
for _, row in df_agent[df_agent['trajectory'] == 'bad'].iterrows():
    print(f"  Q: {row['question'][:60]}...")
    print(f"  Suggestion: {row['trajectory_suggestion']}")
    print()
```

The judge gives you not only a score but also a suggestion for
improvement. This helps you understand what to fix.


## Combining simple and LLM checks

For a comprehensive view, combine both:

```python
for i, result in agent_results.items():
    issues = []
    if result['has_duplicates']:
        issues.append('duplicates')
    if result['num_calls'] > 5:
        issues.append('excessive')
    if result['trajectory'] == 'bad':
        issues.append('llm_flagged')

    result['issues'] = issues

clean = sum(1 for r in agent_results.values() if not r['issues'])
total = len(agent_results)
print(f"Clean trajectories: {clean}/{total}")
```

Simple checks are fast and deterministic. LLM checks are more nuanced
but slower and less consistent. Using both gives you the best coverage.

[<- Collecting Agent Data](06-agent-data.md) | [Instruction Following ->](08-instruction-following.md)
