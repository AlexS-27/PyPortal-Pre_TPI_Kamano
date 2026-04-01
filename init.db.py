"""
File : init.db.py
Description : This file contains the creation of the database
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 3 February 2026
"""

import sqlite3

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

        print(f"✔️ Database '{db_name}' has been created and initialized!")

    except FileNotFoundError:
        print(f"❌ Error: '{sql_file}' not found. Make sure the file exists.")
    except sqlite3.Error as e:
        print(f"❌ SQLite Error: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()