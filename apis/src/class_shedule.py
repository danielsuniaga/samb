from decouple import config

class class_shedule:

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.shedule_permission = config("SHEDULE_PERMISSION")

    def get(self,hour):

        try:

            # string = "SELECT samb_shedule.id AS id FROM samb_shedule WHERE samb_shedule.start_date<=%s AND samb_shedule.end_date>=%s AND samb_shedule.description=%s AND samb_shedule.CONDITION=%s LIMIT 1",[hour,hour,self.shedule_permission,'1']

            _count=self.cursor_db.execute("SELECT samb_shedule.id AS id FROM samb_shedule WHERE samb_shedule.start_date<=%s AND samb_shedule.end_date>=%s AND samb_shedule.description=%s AND samb_shedule.CONDITION=%s LIMIT 1",[int(hour),int(hour),self.shedule_permission,'1'])

            return {'status':True,'msj':'Success'} if _count>0 else {'status':False,'msj': "Horario no contemplado"}

            # return string

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de Shedule "+str(err)}

