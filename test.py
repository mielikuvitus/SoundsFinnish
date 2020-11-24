from werkzeug.security import generate_password_hash, check_password_hash
import time
from models.user import User
from models.user_activity import UserActivity

""" name = 'moi'
user_result = User.get_by_username(name)
if user_result is not None:
    print(user_result.name) """

user_id = '40aab'
user_id_result = User.get_by_user_id(user_id)
if user_id_result is not None:
    print(user_id_result.user_id)