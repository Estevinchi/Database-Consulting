from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from app.controllers.auth_controller import AuthControl

from app.models.model_query import QueryModel

from app.services.user_service import AuthService

from app.routes.admin_routes import is_admin

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")
auth_service = AuthService()

@auth_bp.route("/")
@login_required
def home():
    try:
        niveles = QueryModel.get_niveles()
        tabla = QueryModel.load_top()
        columnas = list(tabla.columns)
        datos = tabla.to_dict(orient="records")
        grupos = QueryModel.get_grupos()
        ciudades = QueryModel.get_municipios()
        return render_template('home.html',columnas=columnas, datos=datos, niveles=niveles, grupos=grupos,municipios=ciudades)
    except Exception:
        flash(f"Error al cargar la tabla excel", "error")
        return redirect(url_for('admin_bp.home_admin'))
    

@auth_bp.route("/user/update/password", methods=['POST'])
@login_required
def update_password():
    if not is_admin():
        flash("No tienes permisos de administrador.")
        return redirect(url_for('auth_bp.home'))
    actual_password=request.form.get('actual_pswd')
    password = request.form.get('password')
    password_check = request.form.get('password_check')
    print(id)
    try:
        if AuthControl.password_change(id, actual_password) != True:
            flash("Contraseña actual incorrecta.")
            return redirect(url_for('auth_bp.user'))
        if password != password_check:
            flash('Error. Las contraseñas no coinciden.', 'error')
            return redirect(url_for('auth_bp.user'))
        AuthControl.password_update_control(id, password)
        flash('Contraseña actualizada', 'success')
        return redirect(url_for('auth_bp.user'))
    except Exception:
        flash(f"Error al buscar el usuario y/o contraseña", "error")
        return redirect(url_for('auth_bp.user'))


@auth_bp.route("/user")
@login_required
def user():
    if not is_admin():
        flash("No tienes permisos de administrador.")
        return redirect(url_for('auth_bp.home'))
    return render_template('user.html')

@auth_bp.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        
        try:
            user = AuthControl.login_control(username,password)
        except Exception:
            flash("Error de control de usuario/contraseña","error")
            return redirect(url_for('auth_bp.login'))
        
        if user is None:
            flash('Usuario y/o contraseña incorrectas','error')
            return redirect(url_for('auth_bp.login'))
        try:
            login_user(user)
            return redirect(url_for('auth_bp.home'))
        except Exception:
            flash("Error de login de usuario/contraseña","error")
            return redirect(url_for('auth_bp.login'))
    if current_user.is_authenticated:
        return redirect(url_for('auth_bp.home'))
    return render_template("login.html")

@auth_bp.route("/logout", methods=['POST'])
@login_required
def logout():
    try:
        logout_user()
        return redirect(url_for('auth_bp.login'))
    except Exception:
        flash("Error de control de usuario/contraseña","error")
        return redirect(url_for('auth_bp.home'))
    

