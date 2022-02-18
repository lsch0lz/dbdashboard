from controller.database import get_conn

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