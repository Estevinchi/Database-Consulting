from app.models.entities.User import User
from app.models.model_user import UserModel



class AdminController():
    
    @staticmethod
    def create_user(username, password, admin):
        new_user= User(username=username, admin=admin)
        new_user.set_password(password)
        inserting = UserModel.insert_user(new_user)
        if inserting != True:
            return False
        return True


    @staticmethod
    def delete_user(id):
        UserModel.delete_user(id)
        
    @staticmethod
    def update_user(id, username,admin):
        update = UserModel.update_user(id, username,admin)
        return update
