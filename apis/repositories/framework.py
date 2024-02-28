from decouple import config

class repositories_framework:

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.condition  = config("CONDITION")

    def get(self):

        return {'status':True,'msj':'Success'}
    
    def add(self,id_framework,fecha,description):

        try:

            self.cursor_db.execute("INSERT INTO samb_framework(samb_framework.id,samb_framework.description,samb_framework.registration_date,samb_framework.condition)values(%s,%s,%s,%s)",[id_framework,description,fecha,self.condition])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_framework: '+str(err)}

        return {'status':True,'msj':'Success'}

