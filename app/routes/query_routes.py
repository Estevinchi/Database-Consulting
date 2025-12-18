from flask import render_template, request, redirect, url_for, flash, Blueprint, send_file

# Models
from app.models.model_query import QueryModel

# Services
from app.services.excel_service import ExcelService
from app.services.query_service import QueryDB


query_bp = Blueprint('query_bp',__name__, url_prefix="/query/")


@query_bp.route("/busqueda", methods=['GET'])
def search_bar():
    action = request.args.get('action')
    df = QueryModel.load_all()
    query = request.args.get('queryAn')
    level_sel = request.args.get('level')
    name = request.args.get('name')
    last_name_1 = request.args.get('last_name_1')
    last_name_2 = request.args.get('last_name_2')
    tel = request.args.get('tel')
    last_name_order = request.args.get('last_name_order')
    group = request.args.get('group')
    mail=request.args.get('mail')
    municipio_sel=request.args.get('city')
    try:
        if query != '':
            df = QueryModel.query_anotacio(query,df)
        if level_sel != '':
            df = QueryModel.level_filter(level_sel,df)
        if name != '':
            df = QueryModel.name_filter(name,df)
        if last_name_1 != '':
            df = QueryModel.last_name_filter(last_name_1, df)
        if  last_name_2 != '':
            df = QueryModel.last_name_2_filter(last_name_2, df)
        if tel != '':
            df = QueryModel.tel_filter(tel,df)
        if last_name_order:
            df= QueryModel.order_by_cognom(df)
        if group != '':
            df= QueryModel.group_filter(group,df)
        if mail != '':
            df = QueryModel.mail_filter(mail,df)
        if municipio_sel !='':
            df = QueryModel.city_filter(municipio_sel,df)
            
            
        if action == "export":
            return ExcelService.export_excel(df)
        try:
            municipios=QueryModel.get_municipios()
        except Exception:
           flash("Faltan columnas","error")
           return redirect(url_for('auth_bp.home'))
        grupos = QueryModel.get_grupos()
        columnas = list(df.columns)
        datos = df.to_dict(orient="records")
        niveles = QueryModel.get_niveles()
        results=len(datos)
        return render_template('home.html', datos=datos, columnas=columnas, query=query, niveles=niveles, level_sel=level_sel, results=results, name=name, last_name_1=last_name_1, last_name_2=last_name_2, order_by = last_name_order, grupos=grupos, grupo_sel=group, mail=mail, municipios=municipios, municipio_sel=municipio_sel, tel=tel)
    except Exception:
        flash(f"Error al cargar el excel", "error")
        return redirect(url_for('auth_bp.home'))
    
    
