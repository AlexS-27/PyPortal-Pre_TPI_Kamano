import os

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import check_password_hash
from core.db_manager import get_user_by_username, register_user
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
 return "Hello World! PyPortal is running!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if register_user(username, password):
            flash('You have successfully registered! Now you can login!', 'success')
            return redirect(url_for('login'))
        else:
            flash('The username already exist. Please select an other one.', 'danger')
            return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id_user']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('login.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)