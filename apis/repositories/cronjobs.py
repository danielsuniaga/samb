from decouple import config

class repositories_cronjobs:

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.estado = config("ESTADO")

        self.id_api = config("ID_API")

        self.id_financial_asset = config("ID_FINANCIAL_ASSET")

        self.default_execute = config("DEFAULT_EXECUTE")

        self.success_condition = config("SUCCESS_CONDITION")

    def set_id_financial_asset(self,value):

        self.id_financial_asset = value

        return True

    def get(self):

        return {'status':True,'msj':'Success'}
    
    def add(self,id_cronjobs,fecha_actual):

        try:

            self.cursor_db.execute("INSERT INTO samb_cronjobs(samb_cronjobs.id,samb_cronjobs.start_date,samb_cronjobs.end_date,samb_cronjobs.condition,samb_cronjobs.id_samb_api_id,samb_cronjobs.id_samb_financial_asset_id,samb_cronjobs.execution_time)VALUES(%s,%s,%s,%s,%s,%s,%s)",[id_cronjobs, fecha_actual, fecha_actual, self.estado,self.id_api,self.id_financial_asset,self.default_execute])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_cronjobs'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def set_fields(self,end_date,execute_time,id_cronjobs):

        try:

            self.cursor_db.execute("UPDATE samb_cronjobs SET samb_cronjobs.condition=%s,samb_cronjobs.end_date=%s,samb_cronjobs.execution_time=%s WHERE samb_cronjobs.id=%s",[self.success_condition,end_date,execute_time,id_cronjobs])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la sobreescritura en samb_cronjobs'+str(err)}

        return {'status':True,'msj':'Success'}

