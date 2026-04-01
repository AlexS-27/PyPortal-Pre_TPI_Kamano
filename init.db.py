"""
File : init.db.py
Description : This file contains the creation of the database
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 3 February 2026
"""

import sqlite3
import random
from datetime import datetime
from werkzeug.security import generate_password_hash

# Realize with the help of gemini
def seed_database(connection):
    """Insère 15 utilisateurs et des scores pour le test."""
    cursor = connection.cursor()

    users = [
        ("player1", "Pass123!"), ("player2", "Pass456!"),
        ("AimMaster", "SecurePass1!"), ("ShadowSniper", "Sniper2026!"),
        ("QuickClick", "Click12345!"), ("PixelHunter", "Hunt3r!!!"),
        ("VaudPlayer", "Lausanne2026!"), ("PythonLover", "FlaskIsCool!"),
        ("CyberPro", "CyberPass78!"), ("GhostTarget", "GhostInTheShell!"),
        ("NovaStrike", "Nova2026*"), ("EliteGamer", "ElitePass11!"),
        ("StormWalker", "Storm999!"), ("AcePilot", "SkyHigh88!"),
        ("ZeroLag", "NoPing123!"), ("Zombie", "Zombie123!"),
    ]

    print("Seeding data...")
    for username, password in users:
        try:
            # 1. Hachage du mot de passe
            hashed_pw = generate_password_hash(password)

            # 2. Insertion de l'utilisateur
            cursor.execute(
                "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
                (username, hashed_pw, datetime.now().strftime("%Y-%m-%d"))
            )
            user_id = cursor.lastrowid

            # 3. Insertion de scores
            if username in ["player1", "player2"]:
                score_val = random.randint(500, 700)
            else:
                score_val = random.randint(350, 600)

            cursor.execute(
                "INSERT INTO scores (value, archived_at,user_id) VALUES (?, ?, ?)",
                (score_val, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_id)
            )
        except sqlite3.IntegrityError:
            continue  # Passe si l'utilisateur existe déjà

    connection.commit()
    print(" Seed data inserted successfully!")

def initialize_database():
    db_name = 'pyportal.db'
    sql_file = 'shema.sql'

    # 1. Connexion à la base (crée le fichier s'il n'existe pas)
    connection = sqlite3.connect(db_name)

    try:
        # 2. Lecture du fichier SQL
        with open(sql_file, 'r') as f:
            sql_script = f.read()

        # 3. Exécution du script
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

        seed_database(connection)

        print(f"✔️ Database '{db_name}' has been created and initialized!")

    except FileNotFoundError:
        print(f"❌ Error: '{sql_file}' not found. Make sure the file exists.")
    except sqlite3.Error as e:
        print(f"❌ SQLite Error: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()