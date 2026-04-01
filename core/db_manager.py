"""
File : core/db_manager.py
Description : SQLite database manager. Contains SQL queries
                for registration, login, saving of the passwords and profile retrieval.
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 9 March 2026
"""

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, password):
    """
    Function to register user
    :param username:
    :param password:
    :return:
    used for :
    - the registration function
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
    """
     Function to save the score
     :param user_id, score_value:
     :return a boolean value indicating if the score is valid
     used for :
        - the game functions
     """
    conn = sqlite3.connect('pyportal.db')
    # Use row to access to the row easily
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        # Get all the score sort by the highest
        cursor.execute(
            "SELECT id_score, value, archived_at FROM scores WHERE user_id = ? ORDER BY value DESC, archived_at DESC",
            (user_id,)
        )
        existing_scores = cursor.fetchall()

        if len(existing_scores) < 2:
            # If there's less than two score saved, insert the new value
            cursor.execute(
                "INSERT INTO scores (value, user_id) VALUES (?, ?)",
                (score_value, user_id)
            )
        else:
            # there's two score so :
            score_1 = existing_scores[0]  # The best score
            score_2 = existing_scores[1]  # The less high

            # Rule number 1 : If the new one is highest of one saved
            # Replace the smallest (score_2)
            if score_value > score_1['value']:
                cursor.execute(
                    "UPDATE scores SET value = ?, archived_at = CURRENT_TIMESTAMP WHERE id_score = ?",
                    (score_value, score_2['id_score'])
                )

            # Rule number 2 : If the new one is the best one we replace by the oldest saved
            # Note : if the scores identicals we replace the oldest one
            else:
                # Search the oldest 'archived_at'
                cursor.execute(
                    "SELECT id_score FROM scores WHERE user_id = ? ORDER BY archived_at ASC LIMIT 1",
                    (user_id,)
                )
                oldest_id = cursor.fetchone()[0]
                cursor.execute(
                    "UPDATE scores SET value = ?, archived_at = CURRENT_TIMESTAMP WHERE id_score = ?",
                    (score_value, oldest_id)
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
    :param user_id:
    :return score:
    used for :
    - the home page functions
    """
    conn = sqlite3.connect('pyportal.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            "select value from scores where user_id = ? order by archived_at desc limit 1",
        (user_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print(f"Error during getting last score: {e}")
        return 0
    finally:
        conn.close()

def get_leaderboard():
    """
      Function to get the top 10 score
      return : top 10 score
      used for :
      - the leaderboard functions
      """
    conn = sqlite3.connect('pyportal.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        query = """
            SELECT users.username, MAX(scores.value) as high_score
            FROM users
            JOIN scores ON users.id_user = scores.user_id
            GROUP BY users.id_user
            ORDER BY high_score DESC
            LIMIT 10
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        conn.close()
