# Agent Evaluation

In module 03, we built agents that use tools to answer questions. The
agent loop runs the LLM, checks for function calls, executes them, and
repeats until the LLM gives a final answer.

Evaluating agents is more complex than evaluating RAG. Not only do we
need to check if the answer is correct, but also:

- Is the agent using tools efficiently?
- Is it making unnecessary or duplicate tool calls?
- Is it following the instructions in the developer prompt?

We'll look at three types of agent evaluation:

1. Answer correctness (same as RAG evaluation)
2. Trajectory evaluation (are the tool calls efficient?)
3. Instruction following (does the agent follow its rules?)


## Collecting agent data

To evaluate an agent, we need to log what it does. For each query, we
record:

- The question
- The sequence of tool calls (the trajectory)
- The final answer

Let's set up the agent from module 03 and collect this data:

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

Run the agent and collect the trajectory:

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

Now run it on ground truth questions:

```python
agent_results = {}

for i, rec in enumerate(tqdm(ground_truth_flat[:50])):
    result = agent_with_logging(rec['question'])
    result['document'] = rec['document']
    result['course'] = rec['course']
    agent_results[i] = result
```


## Answer correctness

We already know how to evaluate answer quality. For agents, we use the
same LLM-as-a-judge approach:

```python
for i, result in agent_results.items():
    doc_id = result['document']
    original_doc = doc_idx[doc_id]
    answer_orig = original_doc['answer']

    eval_result = evaluate_aqa(
        question=result['question'],
        answer_orig=answer_orig,
        answer_llm=result['answer']
    )

    result['correctness'] = eval_result.score
    result['correctness_reasoning'] = eval_result.reasoning
```


## Trajectory evaluation

Trajectory evaluation checks if the agent used tools efficiently. A good
trajectory has:

- Relevant search queries
- No duplicate tool calls
- A reasonable number of total calls (not too many)

```python
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

Evaluate trajectories:

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


## Instruction following

The agent's developer prompt contains rules like "ask if there are other
areas the user wants to explore." We can check if the agent follows
these rules.

```python
class InstructionResult(BaseModel):
    reasoning: str = Field(
        description="Step-by-step reasoning about instruction following."
    )
    score: Literal["good", "bad"] = Field(
        description="'good' if instructions were followed, 'bad' if violated."
    )

instruction_instructions = """
You are an expert evaluator. You will be given:
1. The system instructions given to an agent
2. A user question
3. The agent's response

Check if the agent's response follows the instructions. Read the
instructions carefully and check each applicable rule.

Mark "good" if the agent followed its instructions overall.
Mark "bad" only if the agent clearly violated one or more rules.
""".strip()

instruction_prompt = """
=== AGENT INSTRUCTIONS ===
{instructions}

=== USER QUESTION ===
{question}

=== AGENT ANSWER ===
{answer}
""".strip()

def evaluate_instructions(question, answer, model="gpt-5.4-mini"):
    prompt = instruction_prompt.format(
        instructions=developer_prompt,
        question=question,
        answer=answer
    )

    messages = [
        {"role": "developer", "content": instruction_instructions},
        {"role": "user", "content": prompt}
    ]

    response = openai_client.responses.parse(
        model=model,
        input=messages,
        text_format=InstructionResult
    )

    return response.output_parsed
```

Evaluate:

```python
for i, result in agent_results.items():
    inst_eval = evaluate_instructions(
        question=result['question'],
        answer=result['answer']
    )

    result['instruction_following'] = inst_eval.score
    result['instruction_reasoning'] = inst_eval.reasoning
```


## Putting it all together

Now we have three evaluation dimensions for each agent run:

```python
df_agent = pd.DataFrame(agent_results.values())

print("Correctness:", (df_agent['correctness'] == 'good').mean())
print("Trajectory:", (df_agent['trajectory'] == 'good').mean())
print("Instructions:", (df_agent['instruction_following'] == 'good').mean())
```

These three metrics give you a comprehensive view of agent quality:

- Correctness: is the answer right?
- Trajectory: is the agent using tools well?
- Instructions: is the agent following its rules?

If correctness is low, the search or LLM might need improvement. If
trajectory is bad, the agent is wasting calls -- maybe the developer
prompt needs better guidance. If instruction following is poor, the
prompt rules might need to be clearer.

For production systems, you'd run these evaluations on a larger dataset
and track the metrics over time as you iterate on the agent.


[<< Previous: LLM as a Judge](05-llm-as-judge)
|
[Next: Next Steps >>](07-next-steps)
