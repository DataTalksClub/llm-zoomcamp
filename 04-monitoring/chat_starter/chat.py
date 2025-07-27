import streamlit as st
from openai import OpenAI
import tools

client = OpenAI()

index = tools.init_index()
search_tool = tools.SearchTool(index)

chat_tools = tools.Tools()
chat_tools.add_tool(search_tool.search, search_tool.search_tool)

developer_prompt = """
You're a course teaching assistant. 
You're given a question from a course student and your task is to answer it.

Use FAQ if your own knowledge is not sufficient to answer the question.

At the end of each response, ask the user a follow up question based on your answer.
""".strip()

# --- Streamlit Chat App ---

st.set_page_config(page_title="Course Chat Assistant", page_icon="💬")
st.title("Course Chat Assistant")

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "developer", "content": developer_prompt},
    ]
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
if "pending_response" not in st.session_state:
    st.session_state.pending_response = False

# Display chat history
for msg in st.session_state.display_messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
    elif msg["role"] == "function_call":
        with st.chat_message("assistant"):
            with st.expander(f"Function call: {msg['name']}({msg['arguments']})"):
                st.markdown(f"**Call:** `{msg['name']}({msg['arguments']})`")
                st.markdown(f"**Output:**\n```json\n{msg['output']}\n```")

# User input
prompt = st.chat_input("Ask a question...")
if prompt:
    # Add user message and set pending_response flag
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    st.session_state.display_messages.append({"role": "user", "content": prompt})
    st.session_state.pending_response = True
    st.rerun()

# Process assistant response if pending
if st.session_state.pending_response:
    chat_messages = st.session_state.chat_messages.copy()
    while True:
        response = client.responses.create(
            model='gpt-4o-mini',
            input=chat_messages,
            tools=chat_tools.get_tools(),
        )
        has_tool_calls = False
        for entry in response.output:
            chat_messages.append(entry)
            if entry.type == "function_call":
                # Call the tool and display result
                result = chat_tools.function_call(entry)
                chat_messages.append(result)
                st.session_state.display_messages.append({
                    "role": "function_call",
                    "name": entry.name,
                    "arguments": tools.shorten(entry.arguments),
                    "output": result["output"],
                })
                has_tool_calls = True
            elif entry.type == "message":
                # Display assistant message
                st.session_state.display_messages.append({
                    "role": "assistant",
                    "content": entry.content[0].text,
                })
        if not has_tool_calls:
            break
    st.session_state.chat_messages = chat_messages
    st.session_state.pending_response = False
    st.rerun()
