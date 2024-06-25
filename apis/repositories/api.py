from decouple import config

from apis.repositories.iapi import irepositories_api

class repositories_api(irepositories_api):

    def __init__(self,cursor):

        self.api_description = config("API_DESCRIPTION")

        self.cursor_db = cursor

        self.count = None

        self.condition = config("CONDITION")

    def get(self):

        try:

            self.count=self.cursor_db.execute("SELECT samb_apis.id AS id FROM samb_apis WHERE samb_apis.description=%s AND samb_apis.condition=%s LIMIT 1",[self.api_description,self.condition])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de la API "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "API Desactivada"}
    
    def get_api_key(self,key,value):

        try:

            self.count=self.cursor_db.execute("SELECT samb_config.id AS id FROM samb_config WHERE samb_config.key=%s AND samb_config.value=%s AND samb_config.condition=%s LIMIT 1",[key,value,self.condition])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de key de la API "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "Origen corrupto"}

