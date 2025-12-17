from app.models.model_user import UserModel
from werkzeug.security import check_password_hash
from app.models.entities.User import User


class AuthService:
    def __init__(self):
        self.user_model=UserModel()
    
    def login(self, username, password):
        user = self.user_model.get_user(username)
        if user is None:
            return None
        password_hash_db = user['password_hash']
        if check_password_hash(password_hash_db, password):
            logged_user=User(id=user['id'], username=user['username'], admin=user['admin'])
            return logged_user
        return None
