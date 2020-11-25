#from werkzeug.security import generate_password_hash, check_password_hash
#import time
#from models.user import User
#from models.user_activity import UserActivity
import sqlite
import uuid

sqlite.setup()

""" name = 'moi'
user_result = User.get_by_username(name)
if user_result is not None:
    print(user_result.name) """

""" user_id = '40aab'
user_id_result = User.get_by_user_id(user_id)
if user_id_result is not None:
    print(user_id_result.user_id) """

""" connection = sqlite.get_connection()
cursor = connection.cursor() """

""" words = [
    dict(name="Moi", description="This is used to greet a Finnish person", translation="Hello"),
    dict(name="Moi moi5", description="This is used to greet a Finnish person", translation="Hello")
]
for word in words:
    cursor.execute("INSERT INTO word VALUES (?,?,?,?,?)", (str(uuid.uuid4()), str(uuid.uuid4()), word["name"], word["description"], word["translation"],))
 """
""" sqlite.close_connection(connection) """
