from collections import deque
import streamlit as st
import os
import uuid
import psycopg2
from psycopg2 import sql
from openai import OpenAI
from datetime import datetime
import logging

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

POSTGRES_DB_PARAMS = {
    'user': 'admin',
    'password': 'admin',
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'dbname': 'chat_monitoring',
    'port': '5432'
}


def create_metrics_db(postgres_db_params: dict):
    default_db_params = postgres_db_params.copy()
    default_db_params['dbname'] = 'postgres'
    try:
        connection = psycopg2.connect(**default_db_params)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{postgres_db_params['dbname']}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                sql.SQL(f"CREATE DATABASE {postgres_db_params['dbname']}"))
            logging.error(
                f"Database {postgres_db_params['dbname']} created successfully!")
        else:
            logging.warning(
                f"Database {postgres_db_params['dbname']} already exists!")
        cursor.close()
        connection.close()
    except Exception as error:
        logging.error(f"Error creating database: {error}")


def create_metrics_table(postgres_db_params: dict):
    try:
        connection = psycopg2.connect(**postgres_db_params)
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS chat_history (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            session_id VARCHAR,
            message_type VARCHAR,
            content TEXT,
            feedback VARCHAR,
            UNIQUE (session_id, message_type, content)
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        logging.warning(
            f"Table chat_history created!")
        connection.close()
    except Exception as error:
        logging.error(f"Error creating table: {error}")


def save_message_to_db(session_id, message_type, content, feedback=None):
    try:
        connection = psycopg2.connect(**POSTGRES_DB_PARAMS)
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO chat_history (timestamp, session_id, message_type, content, feedback)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (session_id, message_type, content)
        DO UPDATE SET feedback = EXCLUDED.feedback
        '''
        cursor.execute(insert_query, (datetime.now(), session_id,
                       message_type, content, feedback))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as error:
        logging.error(f"Error saving message to database: {error}")


def update_feedback_in_db(session_id, message_type, content, feedback):
    try:
        connection = psycopg2.connect(**POSTGRES_DB_PARAMS)
        cursor = connection.cursor()
        update_query = '''
        UPDATE chat_history
        SET feedback = %s
        WHERE session_id = %s AND message_type = %s AND content = %s
        '''
        cursor.execute(
            update_query, (feedback, session_id, message_type, content))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as error:
        logging.error(f"Error updating feedback in database: {error}")


# Initialize database and table
create_metrics_db(POSTGRES_DB_PARAMS)
create_metrics_table(POSTGRES_DB_PARAMS)

# Initialize session state variables
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'messages' not in st.session_state:
    st.session_state.messages = deque()
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}

# Set up OpenAI API key


def get_response(message):
    # response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
    #                                           messages=message,
    #                                           max_tokens=150)
    # return response.choices[0].message.content.strip()
    return 'hello' + str(uuid.uuid4())


def clear_chat():
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages.clear()
    st.session_state.feedback.clear()


st.title("Chat with LLM")

# Display session ID
st.write(f"**Session ID:** {st.session_state.session_id}")

# Display chat history
for idx, message in enumerate(st.session_state.messages):
    st.write(f"**{message['role']}:** {message['content']}")
    if message['role'] == 'assistant':
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍", key=f"thumbs_up_{idx}"):
                st.session_state.feedback[idx] = 'thumbs_up'
                update_feedback_in_db(
                    st.session_state.session_id, message['role'], message['content'], 'thumbs_up')
        with col2:
            if st.button("👎", key=f"thumbs_down_{idx}"):
                st.session_state.feedback[idx] = 'thumbs_down'
                update_feedback_in_db(
                    st.session_state.session_id, message['role'], message['content'], 'thumbs_down')

# Chat input
user_input = st.text_input("You:", key="input")
if st.button("Send"):
    if user_input:
        st.session_state.messages.append(
            {'role': 'user', 'content': user_input})
        save_message_to_db(st.session_state.session_id, 'user', user_input)
        response = get_response(st.session_state.messages)
        st.session_state.messages.append(
            {'role': 'assistant', 'content': response})
        save_message_to_db(st.session_state.session_id, 'assistant', response)
        st.rerun()

# Clear chat button
if st.button("Clear Chat"):
    clear_chat()
    st.rerun()

# Display feedback (for debugging purposes)
st.write("### Feedback Data")
st.write(st.session_state.feedback)
