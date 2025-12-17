from app.services.query_service import QueryDB

class QueryModel:
    
    @staticmethod
    def load_all():
        return QueryDB.select_all()
    
    @staticmethod
    def load_top():
        return QueryDB.select_top()
    
    @staticmethod
    def get_niveles():
        lista_niveles = []
        niveles = QueryDB.get_niveles()
        for nivel in niveles:
            nivel = str(nivel)
            if nivel == "nan":
                continue
            lista_niveles.append(nivel)
        return lista_niveles
    
    @staticmethod
    def get_grupos():
        return QueryDB.get_grupos()
    
    @staticmethod
    def get_municipios():
        return QueryDB.get_all_municipi()
# ---------ORDENAR---------------
    @staticmethod
    def order_by_cognom(df_new):
        return QueryDB.order_by_cognom(df_new)



# ---------FILTROS---------------

    @staticmethod
    def query_anotacio(query,df_new):
        return QueryDB.query_anotacio(query,df_new)
    
    @staticmethod
    def level_filter(lvl,df_new):
        return QueryDB.get_by_nivell(lvl,df_new)
    
    @staticmethod
    def name_filter(name,df_new):
        return QueryDB.get_by_nom(name,df_new)
    
    @staticmethod
    def last_name_filter(last_name,df_new):
        return QueryDB.get_by_cognom1(last_name,df_new)
    
    @staticmethod
    def last_name_2_filter(last_name2,df_new):
        return QueryDB.get_by_cognom2(last_name2,df_new)
    
    @staticmethod
    def tel_filter(tel,df_new):
        return QueryDB.get_by_mobil(tel,df_new)
   
    @staticmethod
    def group_filter(group,df_new):
        return QueryDB.get_by_grup(group,df_new)
    
    @staticmethod
    def mail_filter(mail,df_new):
        return QueryDB.get_by_email(mail,df_new)
    
    @staticmethod
    def city_filter(city,df_new):
        return QueryDB.get_by_municipi(city,df_new)
        
    