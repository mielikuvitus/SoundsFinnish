__author__='suvihelin'

import uuid
import sqlite3
import sqlite
from urllib.parse import unquote

class Word(object):

    def __init__(self, lesson_id, name, description, translation, word_id=None):
        self.lesson_id = lesson_id
        self.name = name
        self.description = description
        self.translation = translation
        self.word_id = str(uuid.uuid4()) if word_id is None else word_id
    
    @classmethod
    def find_by_lesson_id(cls, lesson_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by lesson_id
        cursor.execute('SELECT * FROM word WHERE lesson_id =?', (lesson_id,))
        result = cursor.fetchall()
        sqlite.close_connection(connection)

        if result is not None:
            return [cls(row[1], row[2], row[3], row[4], row[0]) for row in result]
        else:
            print("The lesson_id does not exist")
            return None

