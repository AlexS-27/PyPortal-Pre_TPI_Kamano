
PyPortal/
├── api/                            # API REST pour Pygame
│   └── routes.py               # Endpoints (POST score, GET ranking)
├── core/                           # Logique métier et base de données
│   ├──  auth.py                 # Permet de transformer le dossier en module
│   └── db_manager.py     # Fonctions pour gérer les Users et Scores
├── docs                           # Contient tout les documents lier au project
└── game/                        # Jeu Pygame
    ├── main.py              # Code principal du jeu
    └── assets/                # Images et sons du jeu (images, wav, etc.)
├── .venv/                         # Environnement virtuel (créé par PyCharm)
├── web/                         # Interface Web (Flask)
│   ├── static/                  # Fichiers statiques (CSS, JS, Images Web)
│   │   └── style.css
│   └── templates/           # Fichiers HTML
├── app.py                       # Point d'entrée principal Flask
├── init_db.py                  # Script d'initialisation
├── pyportal.db               # Le fichier de base de données SQLite
├── requirements.txt       # Liste des bibliothèques (Flask, Pygame, etc.)
├── schema.sql                # Script SQL de création des tables

