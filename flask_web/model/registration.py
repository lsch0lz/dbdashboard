from controller.database import get_conn

from controller.encryption import hash_password

# registers a new user to the database
# TODO: hash the password
def create_user(name: str, lastname: str, email: str, password: str):
    password_ = hash_password(password)

    conn = get_conn()
    cursor = conn.cursor()
    query = "INSERT INTO users(name, lastname, email, password) VALUES (%s, %s, %s, %s)"
    val = (name, lastname, email, password_)
    cursor.execute(query, val)
    conn.commit()
    return None