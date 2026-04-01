# PyPortal

---
## Description

---
Le projet consiste à développer une application interactive complète, combinant jeu, backend, base de données et interface web, permettant à un utilisateur de :

1. S’inscrire ou se connecter via une interface web Flask.
2. Lancer un mini-jeu Pygame (ex. : test de réflexe, clic sur cibles, esquive d’obstacles).
3. À la fin de la partie, le score est automatiquement envoyé au serveur Flask et enregistré dans une base de données SQLite.
4. L’interface web affiche ensuite un classement en temps réel des meilleurs scores.


L’objectif est de démontrer la capacité à intégrer plusieurs technologies (Pygame, Flask, SQLite, API REST) dans une application cohérente, fonctionnelle et sécurisée, tout en respectant les bonnes pratiques de développement.

## Fonctionnalités principales de l'application

---
Authentification complète :

* Inscription : nom d’utilisateur, mot de passe (haché), email (optionnel).
* Connexion : vérification des identifiants, session utilisateur.
* Suppression de compte : suppression des données utilisateur et scores associés

Base de données relationnelle (SQLite) :

* Table utilisateurs : id, username, password_hash, email, date_inscription.
* Table scores : id, utilisateur_id, score, date_partie.
* Clés étrangères et contraintes d’intégrité.

Mini-jeu Pygame :

* Jeu simple et rapide (ex. : clic sur cibles apparaissant aléatoirement, test de réflexe, esquive d’obstacles).
* Génération d’un score à la fin de la partie (ex. : nombre de clics réussis, temps écoulé, points).
* Envoi automatique du score vers le serveur Flask via API REST (POST /api/score).
* Affichage du score final dans le jeu avant retour à l’interface web.

Application Flask :

* Page d’accueil : connexion / inscription.
* Tableau des scores : affichage des 10 meilleurs joueurs (nom, score, date).
* API REST documentée avec Swagger :
  * GET /api/users → récupérer les profils
  * POST /api/score → envoyer un score
  * GET /api/leaderboard → lire le classement
  * DELETE /api/user/{id} → supprimer un compte
  * POST /api/login → connexion
  * POST /api/register → inscription
* Documentation Swagger accessible via /swagger (interface interactive).

Interface web :

* HTML/CSS simple, clair, accessible.
* Design responsive (adapté aux écrans mobiles et PC).
* Classement mis à jour dynamiquement (via rafraîchissement automatique).
* Affichage du nom de l’utilisateur connecté.

Connexion entre jeu et backend :

* Le jeu Pygame envoie le score via requests.post() vers l’endpoint Flask.
* Le serveur Flask vérifie l’authenticité de l’utilisateur (via token ou session).
* Le score est enregistré dans la base de données.
* Le jeu affiche un message de confirmation (ex. : “Score enregistré !”).

## Pour commencer

---
### Prérequis
* Base de donnée : SQLite 
* Technologie : Python 3.12
* Bibliothèquea : Flask 3.1.2, Pygame 2.6.1, Flasgger (Swagger)
* OS supportée : Windows 11/MacOs
* Outil de versioning : Git 2.51.2
* IDE : PyCharm 2025.2.4 Professionnel
* Navigateur de test : Microsoft Edge
* Gestionnaire de paquets : pip 25.3

---
## Installation (Manuel Technique)
1. **Clonage/Extraction :** Placez le dossier `PyPortal-Pre_TPI_Kamano` sur votre espace de travail.
2. **Environnement Virtuel :**
   ```
   python -m venv .venv
   # Activer l'environement
   source .venv/bin/activate #macOS
   .venv\Scripts\Activate     #Windows
3. **Installation des dépendances :** `pip install -r requirements.txt`
4. **Initialisation :** Création de la base de données => `python init.db.py`
5. **Lancement :** `python app.py`  
---

## Structure du répertoire

---

````PyPortal-Pre_TPI_Kamano/
├── .github/
│   └── workflows/
│       └── ci.yml          
├── core/
│   ├── blacklist.txt                        
│   ├──  auth.py               
│   └── db_manager.py   
├── docs/                    
├── game/
│   ├── base_settings.py
│   ├── effects.py          
│   ├── main.py          
│   └── targets.py
├── htmlcov/
├── templates/
│   ├── base.html
│   ├── homePage.html
│   ├── leaderboard.html
│   ├── login.html
│   └── register.html
├── tests/
│   └── test_utils.py 
├── .venv/                         
├── web/                       
│   ├── static/           
│   │   └── style.css
│   └── templates/
├── .gitignore    
├── app.py                    
├── init_db.py                
├── pyportal.db
├── README.md          
├── requirements.txt       
├── schema.sql               
````
---
## Guide d'utilisation

A. **Navigation :** Accédez à `http://127.0.0.1:5000` via Microsoft Edge ou Opéra.
B. **Cycle de jeu**
 1. **Compte :** Créez un compte depuis register puis connectez-vous.
 2. **Partie :** Cliquez sur "Start Playing". Une fenêtre pygame s'ouvre.
 3. **Objectifs :** Cliquez sur les cibles, un timer de 30 secondes gère la fin de partie.
 4. **Score :** A la fermeture du jeu, retournez sur la page web et votre dernier score sera mis à jour (seul les deux meilleurs score ou plus récent sont enregistré)

---
## Dépannage 

* **Erreur ModuleNotFoundError :** Vérifiez que le .venv est activé
* **Affichage Mac :** Si la fenêtre pygame ne s'affiche pas, vérifiez dans app.py que use_reloader=False est bien présent
* **Swagger :** La documentation est diponible sur `http://127.0.0.1:5000/apidocs/

---
### Convention
Commit Ce projet utilise les Conventional Commits. Les mots principaux étant: "feat, fix, chore, refactor, test, docs" en anglais pour ce projet.

Workflow Ce projet utilise Git. Les branches utilisés sont les suivantes: main, develop, feature, release, hotfix. Les noms des branches suivent ce pattern: type/shortDescription eg.(feature/awesomeFeature).

Prenez le temps de lire quelques fichiers README et trouvez la manière dont vous aimeriez aider d'autres développeurs à collaborer avec vous.

* Il faut savoir :
  * Comment proposer une nouvelle feature (issue, pull request)
  * [Comment commit](https://www.conventionalcommits.org/en/v1.0.0/)
  * [Comment utiliser votre flux de travail](https://nvie.com/posts/a-successful-git-branching-model/)
## Contact

---
| Développeur      | Email                    |                    
|------------------|--------------------------|
|Alex Jason Kamano | <alex.kamano@eduvaud.ch> |
