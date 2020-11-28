__author__='suvihelin'

import uuid
import sqlite3
import sqlite
from models.word import Word

class Lesson(object):

    def __init__(self, name, description, lesson_id=None):
        self.name = name
        self.description = description
        self.lesson_id = str(uuid.uuid4()) if lesson_id is None else lesson_id

    @classmethod
    def get_by_lesson_id(cls, lesson_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by lesson_id
        cursor.execute('SELECT * FROM lesson WHERE lesson_id =?', (lesson_id,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)

        if result is not None:    
            return cls(result[1], result[2], result[0])
        else:
            print("The lesson_id does not exist")
            return None
    
    def get_words(self):
        return Word.find_by_lesson_id(self.lesson_id)
