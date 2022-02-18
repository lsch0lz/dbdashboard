import mysql.connector
from mysql.connector import Error

# returns connection to database 'dbdashboard'
def get_conn() -> mysql.connector.connection_cext.CMySQLConnection:
    try:
        conn = mysql.connector.connect(host='db',
                                             database='dbdashboard',
                                             user='root',
                                             password='root')
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)

# registers a new user to the database
# TODO: hash the password
def create_user(name: str, lastname: str, email: str, password: str):
    conn = get_conn()
    cursor = conn.cursor()
    query = "INSERT INTO user(name, lastname, email, password) VALUES (%s, %s, %s, %s)"
    val = (name, lastname, email, password)
    cursor.execute(query, val)
    conn.commit()
    return None