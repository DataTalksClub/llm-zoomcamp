from gitsource import GithubRepositoryDataReader, chunk_documents
import minsearch
from dotenv import load_dotenv
from openai import OpenAI
from toyaikit.llm import OpenAIClient
from toyaikit.tools import Tools
from toyaikit.chat import IPythonChatInterface
from toyaikit.chat.runners import OpenAIResponsesRunner, DisplayingRunnerCallback

load_dotenv()  # Load environment variables from .env file
client = OpenAI()

# The homework asks us to use a fixed Git commit so everyone works with
# exactly the same version of the course lesson files.
reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

# reader.read() downloads the repository at the chosen commit and returns
# file-like objects for the matching markdown lesson files.
files = reader.read()

documents = []

# file.parse() converts each file into a normal Python dictionary with fields
# such as "filename" and "content".
for file in files:
    doc = file.parse()
    documents.append(doc)

print("Number of lesson pages:", len(documents))
print("Example document keys:", documents[0].keys())
print("Example filename:", documents[0]["filename"])



# minsearch builds a small in-memory search index.
# text_fields are fields where full-text search should happen.
# keyword_fields are metadata fields we may want to keep, filter by, or inspect.
index = minsearch.Index(
    text_fields=["content"],
    keyword_fields=["filename"],
)

# fit() loads the documents into the search index.
# After this, minsearch can rank documents by how relevant they are to a query.
index.fit(documents)

query = "How does the agentic loop keep calling the model until it stops?"

# search() returns a ranked list of matching documents.
# The first item is the highest-ranked result according to minsearch.
results = index.search(query)

print("\nQ2 first result filename:", results[0]["filename"])
print("Q2 first result keys:", results[0].keys())

def search(query: str) -> list[dict]:

    """

    Search the lesson index for documents relevant to the user's question.

    This wraps minsearch behind a small function so the rest of the RAG code

    does not depend directly on minsearch's API. Later, the same kind of

    function becomes a callable tool for the agent.

    """

    return index.search(query, num_results=5)

def build_context(search_results: list[dict]) -> str:

    """

    Convert retrieved lesson documents into one plain-text context block.

    The LLM receives text, not Python dictionaries. This function keeps the

    filename next to the content so the model has source context available.

    """

    context_parts = []

    for doc in search_results:

        context_part = f"""

filename: {doc["filename"]}

content: {doc["content"]}

""".strip()

        context_parts.append(context_part)

    return "\n\n---\n\n".join(context_parts)

def build_prompt(question: str, context: str) -> str:

    """

    Build the exact prompt sent to the model.

    The instruction tells the model to answer only from the retrieved lesson

    context. This is the generation step in Retrieval-Augmented Generation.

    """

    return f"""

You're a course teaching assistant.

Answer the student's question using only the context below.

If the context does not contain the answer, say that the course context does not contain enough information.

Question:

{question}

Context:

{context}

""".strip()

def rag(question: str):

    """

    Run the full RAG pipeline.

    Steps:

    1. Retrieve relevant lesson pages.

    2. Convert them into context.

    3. Build a grounded prompt.

    4. Send the prompt to the model.

    5. Return the answer and usage so we can inspect token counts.

    """

    search_results = search(question)

    context = build_context(search_results)

    prompt = build_prompt(question, context)

    response = client.responses.create(

        model="gpt-5.4-mini",

        input=prompt,

    )

    return response.output_text, response.usage

answer, usage = rag(query)

print("\nQ3 answer:")

print(answer)

print("\nQ3 usage:")

print(usage)

print("\nQ3 input tokens:", usage.input_tokens)

# Q4: Chunk the lesson documents.
#
# Whole lesson pages are large. Chunking splits each page into smaller overlapping
# text windows so retrieval can return only the most relevant part of a lesson
# instead of the entire lesson.
#
# size=2000 means each chunk contains up to 2000 characters.
# step=1000 means the next chunk starts 1000 characters after the previous one.
# Because step is smaller than size, neighbouring chunks overlap by 1000 characters.
chunks = chunk_documents(documents, size=2000, step=1000)

print("\nQ4 number of chunks:", len(chunks))
print("Q4 example chunk keys:", chunks[0].keys())
print("Q4 example chunk filename:", chunks[0]["filename"])
print("Q4 example chunk start:", chunks[0]["start"])
print("Q4 example chunk content length:", len(chunks[0]["content"]))

# Q5: Build a second index over chunks instead of full lesson pages.
#
# This index has the same schema as before:
# - content is searchable text
# - filename is metadata
#
# Difference:
# The records are now smaller chunks, so retrieved context should be shorter.
chunk_index = minsearch.Index(
    text_fields=["content"],
    keyword_fields=["filename"],
)

chunk_index.fit(chunks)


def search_chunks(query: str) -> list[dict]:
    """
    Search the chunk index for smaller passages relevant to the user's question.

    This is the chunked version of the earlier `search` function. It should
    return shorter context because each result is a 2000-character window rather
    than a full lesson page.
    """
    return chunk_index.search(query, num_results=5)


def rag_with_chunks(question: str):
    """
    Run the same RAG pipeline as Q3, but retrieve chunks instead of full documents.

    This lets us compare token usage between:
    - full-page retrieval from Q3
    - chunk-based retrieval here
    """
    search_results = search_chunks(question)
    context = build_context(search_results)
    prompt = build_prompt(question, context)

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt,
    )

    return response.output_text, response.usage


chunked_answer, chunked_usage = rag_with_chunks(query)

print("\nQ5 chunked answer:")
print(chunked_answer)

print("\nQ5 chunked usage:")
print(chunked_usage)

print("\nQ5 chunked input tokens:", chunked_usage.input_tokens)

token_difference = usage.input_tokens - chunked_usage.input_tokens
token_ratio = usage.input_tokens / chunked_usage.input_tokens

print("\nQ5 fewer input tokens:", token_difference)
print("Q5 token reduction ratio:", token_ratio)


# Q6: Turn search into an agent tool.
#
# Plain RAG calls search once because our code explicitly calls search once.
# Agentic RAG gives the model a search tool and lets the model decide:
# - whether to search
# - what query to search for
# - how many times to search
# - when to stop searching and answer
search_call_count = 0


def search(query: str) -> list[dict]:
    """
    Search the course lesson chunks for passages relevant to the query.

    This function is exposed to the agent as a tool. The type hint and docstring
    help the agent framework describe the tool to the LLM.

    The function uses the chunk index from Q5, not the full-document index,
    because the homework asks the agent to search over chunks.
    """
    global search_call_count

    search_call_count += 1

    print(f"\n[search call {search_call_count}] query: {query}")

    return chunk_index.search(query, num_results=5)


instructions = """
You're a course teaching assistant. Answer the student's question using the
search tool. Make multiple searches with different keywords before answering.
""".strip()

agent_tools = Tools()
agent_tools.add_tool(search)

chat_interface = IPythonChatInterface()
callback = DisplayingRunnerCallback(chat_interface)

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=instructions,
    chat_interface=chat_interface,
    llm_client=OpenAIClient(model="gpt-5.4-mini"),
)

agent_question = "How does the agentic loop work, and how is it different from plain RAG?"

result = runner.loop(
    prompt=agent_question,
    callback=callback,
)

print("\nQ6 search call count:", search_call_count)