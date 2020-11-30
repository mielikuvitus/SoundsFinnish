__author__='suvihelin'

import sqlite3
import time
import uuid
import sqlite

class UserActivityNotFoundError(Exception):
    def __init__(self, message):
        self.message = message

class UserActivity(object):

    def __init__(self, word_id, user_id, timestamp=None, user_activity_id=None):
        self.word_id = word_id
        self.user_id = user_id
        self.timestamp = timestamp if timestamp is not None else int(round(time.time() * 1000))
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

    def is_duplicate(self):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by 
        cursor.execute('SELECT * FROM user_activity WHERE user_id =? AND word_id =?', (self.user_id, self.word_id,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)
        return result is not None

    def get_latest_word_id(user_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by user_id
        cursor.execute('SELECT * FROM user_activity WHERE user_id =? ORDER BY "timestamp" DESC LIMIT 1', (user_id,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)
        if result is not None:
            return result[2]
        return None

    def update_timestamp(self):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        cursor.execute('UPDATE user_activity SET "timestamp" =? WHERE word_id =? AND user_id =? ', (int(round(time.time() * 1000)), self.word_id, self.user_id,))
        sqlite.close_connection(connection)
        return

    def find_latest_lesson_position(user_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM user_activity u JOIN word w ON w.word_id = u.word_id WHERE user_id =? ORDER BY "timestamp" DESC LIMIT 1', (user_id,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)
        if result is not None:
            return result[2], result[5]
        return None

    def user_words(user_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by user_id
        cursor.execute('SELECT * FROM user_activity u JOIN word w ON w.word_id = u.word_id WHERE user_id =? ORDER BY "timestamp" DESC', (user_id,))
        result = cursor.fetchall()
        print(result)
        sqlite.close_connection(connection)
        if result is not None:
            return [row for row in result]
        else:
            print("No words were found")
            return None