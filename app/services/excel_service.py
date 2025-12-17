import os
from werkzeug.utils import secure_filename
import logging
import pandas as pd
from flask import send_file
import io


UPLOAD_FOLDER = 'data/Excels'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class ExcelService:

    @staticmethod
    def upload_excel(file):
        try:
            if file is None:
                return False
            filename = secure_filename(file.filename)
            if not filename:
                return False
            
            NEW_FILENAME = "ExampleDATABASE.xlsx"   # <-- Nombre modificado
            
            for f in os.listdir(UPLOAD_FOLDER): # <-- Aquí vacíamos la carpeta para que no haya confusiones
                file_path = os.path.join(UPLOAD_FOLDER, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    
            filepath = os.path.join(UPLOAD_FOLDER, NEW_FILENAME)
            file.save(filepath)

            return True
        except Exception as ex:
            logging.exception('Error guardando el excel')
            return False
        
    @staticmethod
    def export_excel(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        return send_file(
            output,
            as_attachment=True,
            download_name="resultados_consulta.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )