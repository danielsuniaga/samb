class class_apis:

    api_description = ""

    cursor_db = ""

    def __init__(self,api,cursor):

        self.api_description = api

        self.cursor_db = cursor

    def get(self):

        try:

            _count=self.cursor_db.execute("SELECT samb_apis.id AS id FROM samb_apis WHERE samb_apis.description=%s AND samb_apis.condition=%s LIMIT 1",[self.api_description,'1'])

            return {'status':True,'msj':'Success'} if _count>0 else {'status':False,'msj': "API Desactivada"}

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de la API "+str(err)}

