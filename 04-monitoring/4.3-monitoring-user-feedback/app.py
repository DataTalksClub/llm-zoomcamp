import streamlit as st
import uuid
from collections import deque

from utils.llm_utils import ask_llm
from utils.postgres import (
    POSTGRES_DB_PARAMS,
    create_monitoring_db,
    create_chat_table,
    save_message_to_db,
    update_feedback_in_db
)


POSTGRES_DB_PARAMS["dbname"] = "chat_monitoring"
create_monitoring_db(POSTGRES_DB_PARAMS)
create_chat_table(POSTGRES_DB_PARAMS)

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'messages' not in st.session_state:
    st.session_state.messages = deque()
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}


def clear_chat():
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages.clear()
    st.session_state.feedback.clear()


st.title("Chat with LLM")
st.write(st.session_state)

for idx, message in enumerate(st.session_state.messages):
    st.write(f"**{message['role']}:** {message['content']}")
    if message['role'] == 'assistant':
        col1, col2 = st.columns(2)
        with col1: 
            if st.button("👍", key=f"thumbs_up_{idx}"):
                st.session_state.feedback[idx] = 'thumps_up'
                update_feedback_in_db(POSTGRES_DB_PARAMS, st.session_state.session_id, message['role'], message['content'], 'thumps_up')
        with col2:
            if st.button("👎", key=f"thumbs_down_{idx}"):
                st.session_state.feedback[idx] = 'thumps_down'
                update_feedback_in_db(POSTGRES_DB_PARAMS, st.session_state.session_id, message['role'], message['content'], 'thumps_down')


user_input = st.text_input("You:", key="input")
if st.button("Send"):
    if user_input:
        st.session_state.messages.append({'role': 'user', 'content': user_input})
        save_message_to_db(POSTGRES_DB_PARAMS, st.session_state.session_id, 'user', user_input)
        response = ask_llm("gpt-3.5-turbo-0125", st.session_state.messages)
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        save_message_to_db(POSTGRES_DB_PARAMS, st.session_state.session_id, 'assistant', response)
        st.rerun()

if st.button("Clear Chat"):
    clear_chat()
    st.rerun()
