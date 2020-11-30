__author__='suvihelin'

import uuid
import sqlite3
import sqlite

class Audio(object):

    def __init__(self, word_id, content_url, audio_id=None):
        self.word_id = word_id
        self.content_url = content_url
        self.audio_id = str(uuid.uuid4()) if audio_id is None else audio_id
    
    @classmethod
    def find_by_word(cls, word_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by lesson_id
        cursor.execute('SELECT * FROM audio WHERE word_id =?', (word_id,))
        result = cursor.fetchall()
        sqlite.close_connection(connection)

        if result is not None:
            return [cls(row[1], row[2], row[0]) for row in result]
        else:
            print("The word_id does not exist")
            return None
