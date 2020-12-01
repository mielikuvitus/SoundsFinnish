from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.user_activity import UserActivity
from models.lesson import Lesson
from models.word import Word
from models.audio import Audio
from models.video import Video
from models.test_yourself import TestYourself
import sqlite3
import random
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = 'suv'
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def login():
    lesson1 = Lesson.get_by_lesson_id('3845127e-e6d9-4a15-b6e0-14276ace1cd8')
    lesson2 = Lesson.get_by_lesson_id('618af7ad-3d63-4609-a7f1-50704106b9e4')

    if 'name' in session:
        return render_template("home.html", name = session['name'], lesson1 = lesson1, lesson2 = lesson2)
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("home.html")

@app.route("/signup", methods=['GET'])
def sign_up_template():
    if 'user_id' in session:
        return redirect("/")

    return render_template("sign-up.html")

@app.route("/logout", methods=['GET'])
def logout():
    if 'user_id' not in session:
        return redirect("/")

    User.logout()
    return redirect("/")

@app.route("/signup", methods=['POST'])
def sign_up():
    name = request.form['name']
    password_hash = request.form['password_hash']

    try:
        User(name,generate_password_hash(password_hash)).save_to_db()
    except Exception as e:
        return e.message, 500
    
    return redirect("/")

@app.route("/login", methods=['POST'])
def login_user():
    error = None
    name = request.form['name']
    password = request.form['password_hash']
    lesson1 = Lesson.get_by_lesson_id('3845127e-e6d9-4a15-b6e0-14276ace1cd8')
    lesson2 = Lesson.get_by_lesson_id('618af7ad-3d63-4609-a7f1-50704106b9e4')

    if User.login_valid(name, password):
        return render_template('home.html', name = session['name'], lesson1 = lesson1, lesson2 = lesson2)
    else:
        error = 'Invalid credentials'
        session['name'] = None
        return render_template('login.html', error = error)

@app.route("/<string:lesson_id>/<string:word_id>")
@app.route("/<string:lesson_id>")
def lesson_words(lesson_id, word_id = None):
    words = Word.find_by_lesson_id(lesson_id)

    if word_id is None:
        word_id = UserActivity.get_latest_word_id(session['user_id'])
        if word_id == words[-1].word_id:
            word_id = words[0]

    word_index = 0
    for i, word in enumerate(words):
        if word.word_id == word_id:
            word_index = i
            break
            
    word = words[word_index]
    show_video = False

    user_activity = UserActivity(word.word_id, session['user_id'])
    if user_activity.is_duplicate() is False:
        user_activity.save_to_db()
    else:
        user_activity.update_timestamp()
        show_video = True
    
    audio = Audio.find_by_word(word.word_id)
    audio_url = audio[0].content_url

    video = Video.find_by_word(word.word_id)
    video_url = video[0].content_url

    next_word = None
    if word_index < len(words) - 1:
        next_word = words[word_index + 1]

    return render_template("video.html", lesson_id=lesson_id, show_video=show_video, audio_url=audio_url, video_url=video_url, word=word, next_word=next_word)

@app.route("/lesson")
def latest_lesson_position():
    if 'user_id' not in session:
        return redirect("/")

    latest_position = UserActivity.find_latest_lesson_position(session['user_id'])
    if latest_position is None:
        return redirect("/3845127e-e6d9-4a15-b6e0-14276ace1cd8")
    
    return redirect("/{0}/{1}".format(latest_position[1], latest_position[0]))

@app.route("/test_yourself")
@app.route("/test_yourself/<int:page>")
def test(word_id = None, page = 1):
    if 'user_id' not in session:
        return redirect("/")

    total = 11

    if session['url'] >= total:
        session['url'] = 1
        return redirect('/result')
    
    word_list = Word.get_words()
    user_words = UserActivity.user_words(session['user_id'])
    if len(user_words) < 10:
        return redirect("/message")

    test_choices = []

    # Get the answer
    question_randomiser = random.randint(0, len(user_words)-1)
    print(user_words[question_randomiser])
    test_question_id = user_words[question_randomiser][4]
    test_answer = user_words[question_randomiser][6]
    audio = Audio.find_by_word(test_question_id)
    audio_url = audio[0].content_url

    test_choices.append(test_answer)

    # Get the other options
    test_choice1 = random.randint(0, len(word_list)-1)
    test_choice2 = random.randint(0, len(word_list)-1)
    while word_list[test_choice1].name == word_list[test_choice2].name or word_list[test_choice1].name == user_words[question_randomiser][6] or word_list[test_choice2].name == user_words[question_randomiser][6]:
        test_choice1 = random.randint(0, len(word_list)-1)
        test_choice2 = random.randint(0, len(word_list)-1)

    test_choices.append(word_list[test_choice1].name)
    test_choices.append(word_list[test_choice2].name)
    random.shuffle(test_choices)

    return render_template("test.html", page=page, url=session['url'], next_word=page < total, test_answer=test_answer, test_choices=test_choices, total=total, audio_url=audio_url)

@app.route('/submit_answer', methods=["POST"])
def submit_answer():
    if 'user_id' not in session:
        return redirect("/")

    session["correct_answers"] = request.json["result"]
    if session['url'] <= 11:
        session['url'] = session['url'] + 1
        return redirect("/test_yourself/{0}".format(session['url']))
    else:
        return redirect("/result")

@app.route("/result")
def result():
    if 'user_id' not in session:
        return redirect("/")

    message = TestYourself.get_final_score_message(session["correct_answers"])
    return render_template("result.html", message=message)

@app.route("/message")
def show_message():
    return render_template("message.html")

@app.errorhandler(404)
def not_found(request):
    """Page not found."""
    return make_response(render_template("404.html"), 404)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
