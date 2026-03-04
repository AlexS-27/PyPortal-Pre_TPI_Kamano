"""
File : core/db_manager.py
Description : SQLite database manager. Contains SQL queries
                for registration, login, and profile retrieval.
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 10 Février 2026
"""

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(username, password):
    """
    Function to register user
    :param username:
    :param password:
    :return:
    """
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
    """
    Function to get user by username
    :param username:
    :return user:
    used for :
    - the login function
    """
    conn = sqlite3.connect('pyportal.db')
    conn.row_factory = sqlite3.Row # Utilise le nom de la colonne pour faire les recherche
    cursor = conn.cursor()

    try:
        cursor.execute("select * from users where username = ?",
                       (username,))
        user = cursor.fetchone()
        return user
    finally:
        conn.close()

def save_score(score_value, user_id):

    conn = sqlite3.connect('pyportal.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
        "INSERT INTO scores (value, user_id) VALUES (?, ?)",
    (score_value, user_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error during saving score: {e}")
        return False
    finally:
        conn.close()

def get_last_score(user_id):
    """
    Function to get last score
    """
    conn = sqlite3.connect('pyportal.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            "select * from scores where user_id = ? order by archived_at desc limit 1",
        (user_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else 0
    finally:
        conn.close()


