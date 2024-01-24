class class_cronjobs:

    api_description = ""

    cursor_db = ""

    pares = ""

    id_cronjobs = ""

    id_api = ""

    id_api_financial_asset = ""

    fecha_actual = ""

    estado = ""

    def __init__(self,api,cursor,par,id_cronjobs,fecha,estado):

        self.api_description = api

        self.cursor_db = cursor

        self.pares = par

        self.id_cronjobs = id_cronjobs

        self.fecha_actual = fecha

        self.estado = estado

        self.id_api ="4eb8750c3985432c841bd7616ae6619a"

        self.id_api_financial_asset = "3ea3a3c9534143a29702308fbae83f0e"

    def get(self):

        return {'status':True,'msj':'Success'}
    
    def write(self):

        try:

            self.cursor_db.execute("INSERT INTO samb_cronjobs(samb_cronjobs.id,samb_cronjobs.start_date,samb_cronjobs.end_date,samb_cronjobs.condition,samb_cronjobs.id_samb_api_id,samb_cronjobs.id_samb_financial_asset_id)VALUES(%s,%s,%s,%s,%s,%s)",[self.id_cronjobs, self.fecha_actual, self.fecha_actual, self.estado,self.id_api,self.id_api_financial_asset])

        except:

            return {'status': False, 'message':'No se realizo la escritura en samb_cronjobs'}

        return {'status':True,'msj':'Success'}

