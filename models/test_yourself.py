__author__='suvihelin'

import uuid
import sqlite3
import sqlite
from models.word import Word

class TestYourself(object):

    def __init__(self, name, description, test_id=None):
        self.name = name
        self.description = description
        self.test_id = str(uuid.uuid4()) if test_id is None else test_id

    def get_final_score_message(score):
        message = ""
        if score < 3:
            message = str(score) + "/10." + " Terrible"
        elif score < 6:
            message = str(score) + "/10." + " Mediocre"
        elif score < 8:
            message = str(score) + "/10." + " Above average"
        elif score < 10:
            message = str(score) + "/10." + " So close!"
        else:
            message = str(score) + "/10." + " You have mad learning skills"

        return message

    #Calculate number of questions asked to be displayed on page
    def questions_asked():
        return session['url'] - 1