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
