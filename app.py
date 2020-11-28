from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.user_activity import UserActivity
from models.lesson import Lesson
from models.word import Word
from models.audio import Audio
import sqlite3
import short_url

app = Flask(__name__)
app.secret_key = 'suv'

@app.route("/")
def login():
    lesson1 = Lesson.get_by_lesson_id('3845127e-e6d9-4a15-b6e0-14276ace1cd8')
    lesson2 = Lesson.get_by_lesson_id('618af7ad-3d63-4609-a7f1-50704106b9e4')

    if session['name'] is not None:
        return render_template("home.html", name = session['name'], lesson1 = lesson1, lesson2 = lesson2)
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
    lesson1 = Lesson.get_by_lesson_id('3845127e-e6d9-4a15-b6e0-14276ace1cd8')
    lesson2 = Lesson.get_by_lesson_id('618af7ad-3d63-4609-a7f1-50704106b9e4')

    if User.login_valid(name, password):
        User.login(name)
    else:
        error = 'Invalid credentials'
        session['name'] = None
        return render_template('login.html', error = error)
    
    return render_template('home.html', name = session['name'], lesson1 = lesson1, lesson2 = lesson2)

@app.route("/<string:lesson_id>/<string:word_id>")
@app.route("/<string:lesson_id>")
@app.route("/lesson")
def lesson_words(lesson_id, word_id = None):
    lesson = Lesson.get_by_lesson_id(lesson_id)
    words = Word.find_by_lesson_id(lesson_id)

    word_index = 0
    for i, word in enumerate(words):
        if word.word_id == word_id:
            word_index = i
            
    word = words[word_index]
    audio = Audio.find_by_word(word.word_id)
    audio_url = audio[0].content_url

    next_word = None
    if word_index < len(words) - 1:
        next_word = words[word_index + 1]

    return render_template("lesson.html", lesson_id=lesson_id, audio_url=audio_url, word=word, next_word=next_word)

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)
 


