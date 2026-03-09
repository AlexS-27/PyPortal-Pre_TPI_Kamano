"""
File : app.py
Description : Flask main controller handling routes, authentication
                and session logic for the PyPortal project.
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 10 Février 2026
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import check_password_hash
from core.db_manager import get_user_by_username, register_user, save_score, get_last_score
from functools import wraps
from core.utils import is_password_strong
from game.main import run_game
from multiprocessing import Process, Value

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800 #the session expire after 30 minutes

# With the AI help
# Manage the fact that the user need to be connect to access to the page
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You must be logged in to access this page', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# route to the main page
@app.route('/')
@login_required
def home():
    # Récupérer le score via ton db_manager
    current_user_id = session.get('user_id')
    last_score = get_last_score(current_user_id)

    return render_template(
        "homePage.html",
        username=session['username'],
        last_score=last_score)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        Function to register user
        :param username:
        :param password:
        :return:
        """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        user = get_user_by_username(username)
        # Check the password
        is_strong, message = is_password_strong(password)

        if not is_strong:
            flash(message, 'danger')
            return render_template('register.html')

        if register_user(username, password):
            flash('You have successfully registered! Now you can login!', 'success')
            return redirect(url_for('login'))
        else:
            flash("There's been an error, please retry", 'danger')
            return render_template('register.html')

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
        Function to login user
        :param username:
        :param password:
        :return:
        """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        user = get_user_by_username(username)

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id_user']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
        Function to logout user
    """
    session.clear()
    flash('You have successfully logged out', 'info')
    return redirect(url_for('login'))

# On définit une petite fonction wrapper
def game_wrapper(score_obj):
    score = run_game()
    score_obj.value = score


@app.route('/launch_game')
@login_required
def launch_game():
    # On utilise une valeur partagée pour récupérer le score du processus enfant
    shared_score = Value('i', 0)

    # On lance Pygame dans un nouveau processus
    p = Process(target=game_wrapper, args=(shared_score,))
    p.start()
    p.join()  # On attend que le jeu se ferme

    final_score = shared_score.value

    if save_score(final_score, session['user_id']):
        flash(f"Game Over! Score: {final_score} enregistré.", "info")
    else:
        flash("Erreur lors de la sauvegarde.", "danger")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
