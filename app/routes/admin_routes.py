from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required, current_user

from app.controllers.admin_controller import AdminController

from app.models.model_user import UserModel

from app.services.excel_service import ExcelService

admin_bp = Blueprint('admin_bp',__name__, url_prefix='/admin/')

admin_control = AdminController()

def is_admin():
    if current_user.admin == True:
        return True
    return False

@admin_bp.route("/home")
@login_required
def home_admin():
    if not is_admin():
        flash("No tienes permisos de administrador.")
        return redirect(url_for('auth_bp.user'))

    usuarios = UserModel.get_all_users()
    return render_template('/admin/admin.html', usuarios=usuarios)

@admin_bp.route("/create/user", methods=['GET','POST'])
@login_required
def create_user():
    if is_admin() is False:
        return redirect('auth_bp.home')
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        admin = request.form.get('admin')
        
        admin = bool(admin)
        
        if admin_control.create_user(username=username,admin=admin,password=password):
            flash('Usuario creado correctamente')
            return redirect(url_for('admin_bp.home_admin'))
        
        flash('Usuario ya existente.',"error")
        return  render_template('/admin/create_user.html')
    
    return render_template('/admin/create_user.html')

@admin_bp.route("/delete/user/<int:id>", methods=['POST'])
def delete_user(id):
    admin_control.delete_user(id)
    flash('Usuario eliminado correctamente')
    return redirect(url_for('admin_bp.home_admin'))

@admin_bp.route("/update_user", methods=['POST'])
def update_user():
    try:
        id = request.form['id']
        new_username = request.form['username']
        new_admin = bool(request.form.get('admin'))

        admin_control.update_user(id, new_username, new_admin)

        flash('Usuario actualizado', 'success')
        return redirect(url_for('admin_bp.home_admin'))
    
    except Exception:
        flash(f"Error, no se ha podido actualizar el usuario", "error")
        return redirect(url_for('admin_bp.home_admin'))


@admin_bp.route('/upload', methods=['POST'])
def upload_excel():
    file = request.files['file']
    if ExcelService.upload_excel(file) == True:
        flash('Excel importado correctamente')
        return redirect(url_for('admin_bp.home_admin'))
    flash('Error en cargar el excel')
    return redirect(url_for('admin_bp.home_admin'))