from dataclasses import dataclass

from minsearch import Index
from pydantic_ai import Agent, RunContext


# --------------------------------------------------------------------------- #
# Instructions
# --------------------------------------------------------------------------- #

# The system prompt: the agent's role and behavior. This tells the model
# it's a course teaching assistant, how to use the search tool, and what to
# do with off-topic questions. It's the same prompt we used in Module 1.
INSTRUCTIONS = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches. First perform search, analyze the results 
and then perform more searches. 

The question has to be about the course or its logistics, offtopic questions 
shouldn't be answered. If the search returns nothing, it's likely an off-topic question.
If you can't answer the question using FAQ, don't do it yourself. Only use the 
facts from the FAQ database.

At the end, ask if there are other areas that the user wants to explore.
""".strip()


# --------------------------------------------------------------------------- #
# Dependencies
# --------------------------------------------------------------------------- #

# Pydantic AI uses a dependency container: the objects the agent's tools need
# at runtime. Here the only dependency is the minsearch index. When we run the
# agent we pass deps=SearchDeps(index=...), and tools access it via ctx.deps.
#
# In Module 1, the search function used a global `index` variable directly.
# Here we pass it explicitly through deps so the code has no hidden globals.
@dataclass
class SearchDeps:
    index: Index


# --------------------------------------------------------------------------- #
# The agent
# --------------------------------------------------------------------------- #

# This is where we create the agent. We tell it which model to use, what
# dependencies it needs, and the instructions.
#
# In Module 1, building an agent meant three things:
#   1. The instructions (a developer message we passed manually)
#   2. The tool definition (a `search_tool` dict with a hand-written JSON schema)
#   3. The agent loop (a while loop that called the LLM, checked for function
#      calls, ran make_call, fed the result back, and repeated until done)
#
# Pydantic AI replaces all three:
#   - instructions go directly to the Agent constructor
#   - tools are registered with @faq_agent.tool (no manual JSON schema)
#   - the loop is built into run_sync() — we call it and get the answer back
faq_agent = Agent(
    'openai:gpt-5.4-mini',
    deps_type=SearchDeps,
    instructions=INSTRUCTIONS,
)


# --------------------------------------------------------------------------- #
# The search tool
# --------------------------------------------------------------------------- #

# In Module 1 we defined the tool in two places: a `search()` function that did
# the work, and a `search_tool` dict with a hand-written JSON schema describing
# the parameters for the model. We also wrote a `make_call()` dispatcher that
# read the function name, parsed the JSON arguments, called the right function,
# and formatted the result.
#
# Pydantic AI collapses all of that into one decorated function:
#   - the @faq_agent.tool decorator registers it with the agent
#   - the type hints (query: str) become the JSON schema automatically
#   - the docstring becomes the tool description the model sees
#   - the framework handles parsing arguments and calling the function
#
# The first parameter is always ctx (the run context), which gives access to
# the dependencies via ctx.deps. The rest are the tool's arguments, which the
# model fills in.
@faq_agent.tool
def search(ctx: RunContext[SearchDeps], query: str) -> str:
    """Search the FAQ database for entries matching the given query."""
    boost_dict = {'question': 3.0, 'section': 0.5}
    filter_dict = {'course': 'llm-zoomcamp'}

    # ctx.deps.index is the minsearch index we injected via SearchDeps
    results = ctx.deps.index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
        filter_dict=filter_dict
    )

    return results
