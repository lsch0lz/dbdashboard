import psycopg2
from psycopg2 import Error
import os

# returns connection to database 'dbdashboard'
def get_conn():
    try:
        conn = psycopg2.connect(host=os.getenv('postgres_host'),
                                database=os.getenv('postgres_database'),
                                user=os.getenv('postgres_user'),
                                password=os.getenv('postgres_password'),
                                port=25060)
        return conn
    except Error as e:
        print(f'An Error occurred: {e}')
