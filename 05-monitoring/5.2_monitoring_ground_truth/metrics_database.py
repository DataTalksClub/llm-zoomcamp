import psycopg2
from psycopg2 import sql


def create_metrics_db(postgres_db_params: dict):
    default_db_params = postgres_db_params.copy()
    default_db_params['dbname'] = 'postgres'
    try:
        connection = psycopg2.connect(**default_db_params)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{postgres_db_params['dbname']}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL(f"CREATE DATABASE {postgres_db_params['dbname']}"))
            print(f"Database {postgres_db_params['dbname']} created successfully!")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error creating database: {error}")


def create_metrics_table(postgres_db_params: dict):
    try:
        connection = psycopg2.connect(**postgres_db_params)
        cursor = connection.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS metrics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            metric_a FLOAT,
            metric_b FLOAT,
            metric_c FLOAT
        )
        '''
        cursor.execute(query=create_table_query)
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error creating table: {error}")


# def insert_data(cursor, timestamp, metric_a, metric_b, metric_c):
#     insert_query = sql.SQL('''
#     INSERT INTO metrics (timestamp, metric_a, metric_b, metric_c)
#     VALUES (%s, %s, %s, %s)
#     ''')
#     cursor.execute(insert_query, (timestamp, metric_a, metric_b, metric_c))


# def store_metrics(postgres_client, db_params, metrics_df):
#     connection = None
#     try:
#         for _, row in metrics_df.iterrows():
#             insert_data(cursor, row['timestamp'], row['metric_a'], row['metric_b'], row['metric_c'])

#         connection.commit()
#         print("Metrics stored successfully!")

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(f"Error: {error}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
