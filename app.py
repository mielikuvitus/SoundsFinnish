from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.user_activity import UserActivity
import sqlite3

app = Flask(__name__)
app.secret_key = 'suv'

@app.route("/")
def login():
    if session['name'] is not None:
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup", methods=['GET'])
def sign_up_template():
    return render_template("sign-up.html")

@app.route("/logout", methods=['GET'])
def logout():
    User.logout()
    return redirect("/")

@app.route("/signup", methods=['POST'])
def sign_up():
    name = request.form['name']
    password_hash = request.form['password_hash']
    print(password_hash)

    try:
        User(name,generate_password_hash(password_hash)).save_to_db()
    except Exception as e:
        return e.message, 500
    
    return 'User signed in successfully', 201

@app.route("/login", methods=['POST'])
def login_user():
    error = None
    name = request.form['name']
    password = request.form['password_hash']

    if User.login_valid(name, password):
        User.login(name)
    else:
        error = 'Invalid credentials'
        session['name'] = None
        return render_template('login.html', error = error)
    
    return render_template('home.html', name = session['name'])

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)
 


