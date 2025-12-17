# Factoría create_app()
from flask import Flask, url_for, redirect, render_template
from flask_login import LoginManager

# Importar blueprints
from app.routes.auth_routes import auth_bp
from app.routes.admin_routes import admin_bp
from app.routes.query_routes import query_bp

# Importar modelos
from app.models.model_user import UserModel
from app.models.entities.User import User

login_manager = LoginManager()

def create_app(config_class):

    app = Flask(__name__, template_folder="templates", static_folder='static')
        
    app.config.from_object(config_class)

    # Inicializar LoginManager
    login_manager.init_app(app)
    login_manager.login_view = "auth_bp.login"
    login_manager.login_message = "Por favor, inicie sesión para acceder a esta página."

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(query_bp)

    # Loader de usuarios
    @login_manager.user_loader
    def load_user(user_id):
        user_data = UserModel().get_user_by_id(user_id)
        if not user_data:
            return None
        user_id, username, password_hash, admin = user_data
        loaded_user = User(id=user_id, username=username, admin=admin)
        loaded_user.set_password(password_hash)
        return loaded_user
    
    @app.route("/")
    def start():
        return redirect(url_for('auth_bp.login'))
    
    @app.errorhandler(404)
    def error404(e):
        return render_template('/errors/404.html')

    @app.errorhandler(405)
    def error404(e):
        return render_template('/errors/405.html')
    
    
    @app.errorhandler(500)
    def error500(e):
        return render_template('errors/500.html')
    
    return app