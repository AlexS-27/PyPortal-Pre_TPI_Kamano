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
    # On utilise Row pour accéder facilement aux colonnes par nom
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        # 1. Récupérer les scores actuels de l'utilisateur (triés du plus haut au plus bas)
        cursor.execute(
            "SELECT id_score, value, archived_at FROM scores WHERE user_id = ? ORDER BY value DESC, archived_at DESC",
            (user_id,)
        )
        existing_scores = cursor.fetchall()

        if len(existing_scores) < 2:
            # S'il y a moins de 2 scores, on enregistre simplement le nouveau
            cursor.execute(
                "INSERT INTO scores (value, user_id) VALUES (?, ?)",
                (score_value, user_id)
            )
        else:
            # Il y a déjà 2 scores. On applique tes règles :
            score_1 = existing_scores[0]  # Le meilleur score
            score_2 = existing_scores[1]  # Le moins bon des deux

            # Règle A : Si le nouveau score est meilleur que l'un des deux existants
            # On remplace le plus petit des deux (score_2)
            if score_value > score_1['value']:
                cursor.execute(
                    "UPDATE scores SET value = ?, archived_at = CURRENT_TIMESTAMP WHERE id_score = ?",
                    (score_value, score_2['id_score'])
                )

            # Règle B : Si le score actuel n'est pas meilleur, on remplace le plus ancien
            # Note : Si les deux scores sont égaux au nouveau, on remplace quand même le plus ancien
            else:
                # On cherche le plus ancien des deux via 'archived_at'
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


