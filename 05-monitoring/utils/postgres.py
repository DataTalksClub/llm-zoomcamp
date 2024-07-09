import psycopg2
from psycopg2 import sql
import logging
import os
from datetime import datetime

POSTGRES_DB_PARAMS = {
    'user': 'admin',
    'password': 'admin',
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': '5432'
}

chat_table_sql = '''
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


def create_metrics_table(postgres_db_params: dict, create_table_query: str):
    try:
        connection = psycopg2.connect(**postgres_db_params)
        cursor = connection.cursor()
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
