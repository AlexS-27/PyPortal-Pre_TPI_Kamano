import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(username, password):
    conn = sqlite3.connect('pyportal.db')
    cursor = conn.cursor()

    hashed_pw = generate_password_hash(password)

    try:
        cursor.execute("insert into users (username, password) values (?, ?)",
                       (username, hashed_pw))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect('pyportal.db')
    cursor = conn.cursor()

    try:
        cursor.execute("select * from users where username = ?",
                       (username,))
        user = cursor.fetchone()
        return user
    finally:
        conn.close()
