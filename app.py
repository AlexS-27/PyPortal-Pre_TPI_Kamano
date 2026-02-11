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
from core.db_manager import get_user_by_username, register_user
from functools import wraps
from core.utils import is_password_strong
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
 return "Hello World! PyPortal is running!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        Function to register user
        :param username:
        :param password:
        :return:
        """
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        user = get_user_by_username(username)
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
        username = request.form['username'].strip()
        password = request.form['password'].strip()

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

if __name__ == '__main__':
    app.run(debug=True)