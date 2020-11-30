__author__='suvihelin'

import sqlite3
import uuid
import sqlite
from flask import session
from werkzeug.security import check_password_hash

class UserNotFoundError(Exception):
    def __init__(self, message):
        self.message = message

class UserNameIsInUseError(Exception):
    def __init__(self, message):
        self.message = message

class User(object):

    def __init__(self, name, password_hash, user_id=None):
        self.name = name
        self.password_hash = password_hash
        self.user_id = str(uuid.uuid4()) if user_id is None else user_id


    def save_to_db(self):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        # run a select query against the table to see if any record exists that has the username
        cursor.execute('SELECT name FROM user WHERE name=?',(self.name,))
        result = cursor.fetchone()        
    
        if result:
            raise UserNameIsInUseError('This username is in use. Please select another one.')
        else:
            try:
                #add user data
                cursor.execute('INSERT INTO user (user_id, name, password_hash) VALUES (?, ?, ?)', (self.user_id, self.name, self.password_hash))
                session['name'] = self.name
                session['user_id'] = self.user_id
            except:
                # cursor.execute('CREATE TABLE user (user_id text PRIMARY KEY, name text, password_hash text)')
                raise UserNotFoundError('The table `user` does not exist')
            finally:
                sqlite.close_connection(connection)

    @classmethod
    def get_by_username(cls, name):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by name
        cursor.execute('SELECT * FROM user WHERE name =?', (name,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)

        if result is not None:
            return cls(result[1], result[2], result[0])  
        else:
            print('This username does not exist')
            return None
    
    @classmethod
    def get_by_user_id(cls, user_id):
        #define connection and cursor
        connection = sqlite.get_connection()
        cursor = connection.cursor()

        #get by user_id
        cursor.execute('SELECT * FROM user WHERE user_id =?', (user_id,))
        result = cursor.fetchone()
        sqlite.close_connection(connection)

        if result is not None:    
            return cls(result[1], result[2], result[0])
        else:
            print("The user_id does not exist")
            return None

    @staticmethod
    def login_valid(name, password):
        #Check if username matches with their password
        user = User.get_by_username(name)
        if user is not None:
            #Check password using check_password_method that only compares passwords and doesn't salt them
            if check_password_hash(user.password_hash, password) is True:
                session['name'] = user.name
                session['user_id'] = user.user_id
                session['url'] = 1
                session['score'] = 0
                return True

        return False
    
    @staticmethod
    def logout():
        session['name'] = None
        session['user_id'] = None
        session['url'] = None
        session['score'] = None


