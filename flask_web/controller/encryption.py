from passlib.hash import sha256_crypt
from controller.database import get_conn

# creates hash for user-password
def hash_password(password: str) -> str:
    pwd = sha256_crypt.hash(password)
    return pwd

# checks user input for password
def verify_password(email: str, password_user: str) -> bool:
    conn = get_conn()
    cursor = conn.cursor()

    query = "SELECT password FROM user WHERE email = " + "'" + email + "';"
    cursor.execute(query)
    result = cursor.fetchall()

    # data-manipulation because of formatting
    result_ = result[0]
    result__ = str(result_)[2:-3]

    if sha256_crypt.verify(str(password_user), result__):
        # TODO: redirect to homepage
        return None