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
* Technologie : Python 3.12 (Flask 3.1.2, Pygame 2.6.1)
* OS supportée : Windows 11 Education 24H2
* Outil de versioning : Git 2.51.2
* IDE : PyCharm 2025.2.4 Professionnel
* Navigateur de test : Microsoft Edge
* Gestionnaire de paquets : pip 25.3

### Configuration
Exécuter le fichier de la création de la db dans votre cmd (init.db.py). 

## Déploiement

---

## Structure du répertoire

---

````PyPortal/
├── api/                         
│   └── routes.py             
├── core/                         
│   ├──  auth.py               
│   └── db_manager.py   
├── docs                      
└── game/            
    ├── main.py          
    └── assets/               
├── .venv/                         
├── web/                       
│   ├── static/           
│   │   └── style.css
│   └── templates/      
├── app.py                    
├── init_db.py                
├── pyportal.db               
├── requirements.txt       
├── schema.sql               
````

## Collaboration

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