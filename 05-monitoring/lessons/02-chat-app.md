# Chat App with Feedback

We need a user interface where people can ask questions and give
feedback on the answers. Streamlit is a Python framework that makes it
easy to build web apps with minimal code.

Let's build a chat app that:

- Lets the user select a course and ask a question
- Runs the RAG pipeline and shows the answer
- Has thumbs up / thumbs down buttons for feedback


## Setting up the RAG pipeline

First, the RAG pipeline. This is the same one we built in module 03:

```python
import requests
from minsearch import Index
from openai import OpenAI

openai_client = OpenAI()

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
url_prefix = 'https://datatalks.club/faq'

for course in courses_raw:
    course_url = f'{url_prefix}{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

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

INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()

def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()

def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)
```

The LLM function records response time and token usage:

```python
import time

def llm(instructions, user_prompt, model="gpt-5.4-mini"):
    start_time = time.time()

    input_messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": user_prompt}
    ]
    response = openai_client.responses.create(
        model=model,
        input=input_messages
    )

    response_time = time.time() - start_time
    answer = response.output_text

    tokens = {
        'prompt_tokens': response.usage.input_tokens,
        'completion_tokens': response.usage.output_tokens,
        'total_tokens': response.usage.total_tokens
    }

    return answer, tokens, response_time
```

We also want to evaluate relevance automatically. We use the same
LLM-as-a-judge approach from module 04:

```python
import json

def evaluate_relevance(question, answer):
    prompt_template = """
    You are an expert evaluator for a RAG system.
    Analyze the relevance of the generated answer to the given question.
    Classify it as "NON_RELEVANT", "PARTLY_RELEVANT", or "RELEVANT".

    Question: {question}
    Generated Answer: {answer}

    Provide your evaluation in parsable JSON without using code blocks:

    {{
      "Relevance": "NON_RELEVANT" | "PARTLY_RELEVANT" | "RELEVANT",
      "Explanation": "Brief explanation"
    }}
    """.strip()

    prompt = prompt_template.format(question=question, answer=answer)
    evaluation, _, _ = llm(INSTRUCTIONS, prompt)

    try:
        json_eval = json.loads(evaluation)
        return json_eval['Relevance'], json_eval['Explanation']
    except json.JSONDecodeError:
        return "UNKNOWN", "Failed to parse evaluation"
```

Now the main function that ties it together:

```python
def calculate_cost(model, tokens):
    cost = 0
    if 'gpt-5.4-mini' in model:
        cost = (tokens['prompt_tokens'] * 0.15 + tokens['completion_tokens'] * 0.60) / 1_000_000
    return cost

def get_answer(query, course, model="gpt-5.4-mini"):
    search_results = search(query, course=course)
    prompt = build_prompt(query, search_results)
    answer, tokens, response_time = llm(INSTRUCTIONS, prompt, model=model)

    relevance, explanation = evaluate_relevance(query, answer)
    openai_cost = calculate_cost(model, tokens)

    return {
        'answer': answer,
        'response_time': response_time,
        'relevance': relevance,
        'relevance_explanation': explanation,
        'model_used': model,
        'prompt_tokens': tokens['prompt_tokens'],
        'completion_tokens': tokens['completion_tokens'],
        'total_tokens': tokens['total_tokens'],
        'openai_cost': openai_cost,
    }
```


## Building the Streamlit app

Now the Streamlit interface:

```python
import streamlit as st
import uuid
from assistant import get_answer

st.title("Course Assistant")

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

course = st.selectbox(
    "Select a course:",
    ["data-engineering-zoomcamp", "machine-learning-zoomcamp", "mlops-zoomcamp"],
)

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Processing..."):
        answer_data = get_answer(user_input, course)
        st.success("Completed!")
        st.write(answer_data["answer"])

        st.write(f"Response time: {answer_data['response_time']:.2f}s")
        st.write(f"Relevance: {answer_data['relevance']}")

        save_conversation(
            st.session_state.conversation_id,
            user_input,
            answer_data,
            course
        )
        st.session_state.conversation_id = str(uuid.uuid4())

col1, col2 = st.columns(2)
with col1:
    if st.button("+1"):
        save_feedback(st.session_state.conversation_id, 1)
with col2:
    if st.button("-1"):
        save_feedback(st.session_state.conversation_id, -1)
```

The `save_conversation` and `save_feedback` functions write to PostgreSQL.
We'll implement those in the next lesson.

First, add Streamlit to your project:

```bash
uv add streamlit psycopg psycopg2-binary
```

Then run the app:

```bash
uv run streamlit run app.py
```

You should see a web interface where you can ask questions and give
feedback. Each interaction is saved with the question, answer, response
time, relevance, tokens, and cost.


[<< Previous: Intro](01-intro)
|
[Next: Database >>](03-database)
