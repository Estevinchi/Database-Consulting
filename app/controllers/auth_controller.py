from app.services.user_service import AuthService
from app.models.entities.User import User
from app.models.model_user import UserModel


class AuthControl:
        
    @staticmethod
    def login_control(username, password):
        service = AuthService()
        user_data = service.login(username, password)
        if user_data:
            user = User(user_data.id, user_data.username, user_data.admin)
            return user
        return None
    
    @staticmethod
    def password_update_control(id,password):
        usuario = User(id=id)
        usuario.set_password(password)        
        UserModel.update_pswd(usuario.id, usuario.password_hash)
        
    @staticmethod
    def password_change(id,password):
        actual_pswd=UserModel.get_user_by_id(id)
        check = User.check_password(password_plain=password, hashed_password=actual_pswd["password_hash"])
        return check