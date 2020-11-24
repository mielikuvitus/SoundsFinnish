__author__='suvihelin'

import sqlite3
import time
import uuid
import sqlite

class UserActivityNotFoundError(Exception):
    def __init__(self, message):
        self.message = message

class UserActivity(object):

    def __init__(self, word_id, user_id, timestamp=int(time.time()), user_activity_id=None):
        self.word_id = word_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.user_activity_id = str(uuid.uuid4()) if user_activity_id is None else user_activity_id

    def save_to_db(self):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #add user data
        try:
            cursor.execute('INSERT INTO user_activity (word_id, user_id, timestamp, user_activity_id) VALUES (?, ?, ?, ?)', (self.word_id, self.user_id, self.timestamp, self.user_activity_id))
        except:
            cursor.execute('CREATE TABLE user_activity (user_activity_id text PRIMARY KEY, timestamp integer, word_id text, user_id text, FOREIGN KEY(word_id) REFERENCES word(word_id), FOREIGN KEY(user_id) REFERENCES user(user_id))')
            raise UserActivityNotFoundError('The table `user_activity` did not exist, but it was created. Run the command again.')
        finally:
            sqlite.close_connection(connection)
