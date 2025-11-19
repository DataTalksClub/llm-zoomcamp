import streamlit as st
from config import QDRANT_HOST, COLLECTION_NAME
from tools import SearchTool, QdrantVectorStore, build_context, OpenAIClient
import os
from openinference.instrumentation.openai import OpenAIInstrumentor
from tracing import tracer

os.environ["TOKENIZERS_PARALLELISM"] = "false"
API_KEY=os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4.1-nano"

# Instrument the OpenAI client automatically
OpenAIInstrumentor().instrument()
qv = QdrantVectorStore(host=QDRANT_HOST)
sv = SearchTool(client=qv.client,
                collection_name=COLLECTION_NAME)
    
dev_prompt_template = """
You are a course assistant, and your goal is to answer questions of students, where QUESTION is provided below and CONTEXT is provided most of the times. 
Rules:
* Answer the QUESTION based on the CONTEXT.
* Use only the facts from the CONTEXT.
* If CONTEXT is empty, please let the student know, the information about their query is not there, however you found the following information on the web, by searching the web

QUESTION: {question}

CONTEXT: {context}
""".strip()

st.set_page_config(page_title="Course Chat Assistant", page_icon="💬")
st.title("Course Chat Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "prompts" not in st.session_state:
    st.session_state.prompts = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask a question..."):
    with st.chat_message("user response"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.markdown(user_input)

    with tracer.start_as_current_span("user_query_received", openinference_span_kind="llm") as llm_span:
        llm_span.set_attribute("llm.input.preview", user_input[:100])
        llm_span.set_attribute("input.value", user_input)

      
        search_results = sv.search_hybrid(query=user_input, 
                                            limit=1,
                                            filter_key="course",
                                            filter_value="mlops-zoomcamp")
        if search_results:
            llm_span.set_attribute("search.result.text", search_results[0].payload["text"])
            context = build_context(search_results)
            prompt = dev_prompt_template.format(question=user_input, context=context)
            llm_span.set_attribute("llm.prompt", prompt)
            st.session_state.prompts.append({"role": "user", "content": prompt})
     
        with st.chat_message("assistant"):
            client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"), model=MODEL)
            stream = client.chat_stream(messages=st.session_state.prompts)
            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
            llm_span.set_attribute("llm.output.preview", response[:100])
            llm_span.set_attribute("output.value", response)