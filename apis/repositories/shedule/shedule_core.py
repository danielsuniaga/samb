from decouple import config

from apis.repositories.shedule.ishedule import irepositories_shedule

class repositories_shedule_core():

    shedule_permission = None

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.count = None

    def get(self,hour):

        try:

            self.count=self.cursor_db.execute("SELECT samb_shedule.id AS id FROM samb_shedule WHERE samb_shedule.start_date<=%s AND samb_shedule.end_date>=%s AND samb_shedule.description=%s AND samb_shedule.CONDITION=%s LIMIT 1",[int(hour),int(hour),self.shedule_permission,'1'])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de Shedule "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count>0 else {'status':False,'msj': "Horario no contemplado"}
