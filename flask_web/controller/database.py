import psycopg2
from psycopg2 import Error
import os

# returns connection to database 'dbdashboard'
def get_conn():
    pwd = os.getenv('postgres_password')
    print(pwd)
    conn = psycopg2.connect(host='app-32a76287-24f4-4343-b19e-c1bcba546d72-do-user-11028986-0.b.db.ondigitalocean.com',
                            database='dbdashboard',
                            user='dbdashboard',
                            password=pwd,
                            port=25060)
    return conn

