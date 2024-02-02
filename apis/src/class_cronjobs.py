from decouple import config

class class_cronjobs:

    def __init__(self):

        self.estado = config("ESTADO")

        self.id_api = config("ID_API")

        self.id_financial_asset = config("ID_FINANCIAL_ASSET")

    def get(self):

        return {'status':True,'msj':'Success'}
    
    def write(self,id_cronjobs,fecha_actual,cursor):

        try:

            cursor.execute("INSERT INTO samb_cronjobs(samb_cronjobs.id,samb_cronjobs.start_date,samb_cronjobs.end_date,samb_cronjobs.condition,samb_cronjobs.id_samb_api_id,samb_cronjobs.id_samb_financial_asset_id)VALUES(%s,%s,%s,%s,%s,%s)",[id_cronjobs, fecha_actual, fecha_actual, self.estado,self.id_api,self.id_financial_asset])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_cronjobs'+str(err)}

        return {'status':True,'msj':'Success'}

