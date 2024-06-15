import psycopg2
from psycopg2 import sql
import pandas as pd
from datetime import datetime


DB_PARAMS = {
    'user': 'admin',
    'password': 'admin',
    'host': 'metrics-db',
    'dbname': 'metrics_db',
    'port': '5432'
}

def create_database(db_params):
    default_db_params = db_params.copy()
    default_db_params['dbname'] = 'postgres'
    try:
        connection = psycopg2.connect(**default_db_params)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_params['dbname']}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL(f"CREATE DATABASE {db_params['dbname']}"))
            print(f"Database {db_params['dbname']} created successfully!")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error creating database: {error}")

metrics = {
    'timestamp': [datetime.now(), datetime.now(), datetime.now()],
    'metric_a': [0.95, 0.93, 0.92],
    'metric_b': [0.85, 0.93, 0.92],
    'metric_c': [0.95, 0.94, 0.90],
}
metrics_df = pd.DataFrame(metrics)


def create_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS metrics (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP,
        metric_a FLOAT,
        metric_b FLOAT,
        metric_c FLOAT
    )
    '''
    return create_table_query


def insert_data(cursor, timestamp, metric_a, metric_b, metric_c):
    insert_query = sql.SQL('''
    INSERT INTO metrics (timestamp, metric_a, metric_b, metric_c)
    VALUES (%s, %s, %s, %s)
    ''')
    cursor.execute(insert_query, (timestamp, metric_a, metric_b, metric_c))


def store_metrics(db_params, metrics_df):
    connection = None
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        cursor.execute(create_table())

        for _, row in metrics_df.iterrows():
            insert_data(cursor, row['timestamp'], row['metric_a'], row['metric_b'], row['metric_c'])

        connection.commit()
        print("Metrics stored successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database(DB_PARAMS)
    store_metrics(DB_PARAMS, metrics_df)
