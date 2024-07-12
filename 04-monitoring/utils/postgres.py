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


def execute_db_operation(operation_type, POSTGRES_DB_PARAMS, query, params=None):
    try:
        connection = psycopg2.connect(**POSTGRES_DB_PARAMS)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()
        connection.close()
        if operation_type == 'create_table':
            logging.warning("Table created!")
        else:
            logging.info(
                f"Database operation '{operation_type}' executed successfully!")
    except Exception as error:
        logging.error(f"Error during '{operation_type}': {error}")


def create_metrics_table(POSTGRES_DB_PARAMS):
    chat_table_sql = '''
        CREATE TABLE IF NOT EXISTS metrics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            metric_a FLOAT,
            metric_b FLOAT,
            metric_c FLOAT
        )
        '''
    execute_db_operation(
        'create_table', POSTGRES_DB_PARAMS, chat_table_sql)


def create_chat_table(POSTGRES_DB_PARAMS):
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
    execute_db_operation(
        'create_table', POSTGRES_DB_PARAMS, chat_table_sql)


def save_message_to_db(POSTGRES_DB_PARAMS, session_id, message_type, content, feedback=None):
    insert_query = '''
    INSERT INTO chat_history (timestamp, session_id, message_type, content, feedback)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (session_id, message_type, content)
    DO UPDATE SET feedback = EXCLUDED.feedback
    '''
    params = (datetime.now(), session_id, message_type, content, feedback)
    execute_db_operation('insert', POSTGRES_DB_PARAMS, insert_query, params)


def update_feedback_in_db(POSTGRES_DB_PARAMS, session_id, message_type, content, feedback):
    update_query = '''
    UPDATE chat_history
    SET feedback = %s
    WHERE session_id = %s AND message_type = %s AND content = %s
    '''
    params = (feedback, session_id, message_type, content)
    execute_db_operation('update', POSTGRES_DB_PARAMS, update_query, params)


def insert_data(cursor, timestamp, metric_a, metric_b, metric_c):
    insert_query = sql.SQL('''
    INSERT INTO metrics (timestamp, metric_a, metric_b, metric_c)
    VALUES (%s, %s, %s, %s)
    ''')
    cursor.execute(insert_query, (timestamp, metric_a, metric_b, metric_c))


def store_metrics(POSTGRES_DB_PARAMS, db_params, metrics_df):
    connection = psycopg2.connect(**POSTGRES_DB_PARAMS)
    cursor = connection.cursor()
    try:
        for _, row in metrics_df.iterrows():
            insert_data(
                cursor, row['timestamp'], row['metric_a'], row['metric_b'], row['metric_c'])
        connection.commit()
        print("Metrics stored successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
