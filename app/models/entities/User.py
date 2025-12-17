from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id=None, username=None, admin=False) -> None:
        self.id=id
        self.password_hash=None
        self.username=username
        self.admin=admin
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    
    @staticmethod
    def check_password(hashed_password, password_plain):
        return check_password_hash(hashed_password, password_plain)