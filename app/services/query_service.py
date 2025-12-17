import pandas as pd
import os

DATABASE = "data/Excels/ExampleDATABASE.xlsx"

def load_df():
    """Cargar la BBDD."""
    try:
        if not os.path.exists(DATABASE):
            return pd.DataFrame() 
        df = pd.read_excel(DATABASE).sort_values(by='Fecha', ascending=False)
        df = df.rename(columns={'1_Apellido':'1r Apellido', '2_Apellido':'2n Apellido','correo':'Email'})
        return df
    except Exception as ex:
            return f"Error {ex}"


class QueryDB:

    @staticmethod
    def select_all():
        df = load_df()
        return df

    @staticmethod
    def select_top():
        df = load_df()
        return df.head(10)

    @staticmethod
    def get_niveles():
        df = load_df()
        return set(df['Curso'])

    @staticmethod
    def get_all_municipi():
        df = load_df()
        return set(df['Ciudad'])
    
    @staticmethod
    def get_grupos():
        df = load_df()
        return set(df['Estado'])

    # ---------ORDEN---------------
    @staticmethod
    def order_by_cognom(df_new):
        return df_new.sort_values(by='1r Apellido', ascending=True)

    # ---------FILTROS---------------

    @staticmethod
    def query_anotacio(query, df_new):
        return df_new[df_new['Observaciones'].str.contains(query, na=False, case=False)]

    @staticmethod
    def get_by_nivell(course, df_new):
        return df_new[df_new['Curso'] == course]

    @staticmethod
    def get_by_nom(name, df_new):
        return df_new[df_new['Nombre'].str.contains(name, case=False, na=False)]

    @staticmethod
    def get_by_cognom1(lastName_1, df_new):
        return df_new[df_new['1r Apellido'].str.contains(lastName_1, case=False, na=False)]

    @staticmethod
    def get_by_cognom2(lastName_2, df_new):
        return df_new[df_new['2n Apellido'].str.contains(lastName_2, case=False, na=False)]

    @staticmethod
    def get_by_mobil(tel, df_new):
        return df_new[df_new['Telefono'].astype(str).str.contains(tel, case=False, na=False)]

    @staticmethod
    def get_by_grup(group, df_new):
        return df_new[df_new['Estado'] == group]

    @staticmethod
    def get_by_email(mail, df_new):
        return df_new[df_new['Email'].str.contains(mail, case=False, na=False)]

    @staticmethod
    def get_by_municipi(city, df_new):
        return df_new[df_new['Ciudad'] == city]
