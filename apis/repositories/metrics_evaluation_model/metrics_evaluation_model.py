class repositories_metrics_evaluation_model():

    cursor_db = None

    def __init__(self,cursor):

        self.cursor_db = cursor

    def generate_string(self,data):

        return str(data)

    def add(self,data):

        try:

            self.cursor_db.execute( "INSERT INTO samb_metrics_evaluation_model(samb_metrics_evaluation_model.id,samb_metrics_evaluation_model.type_model,samb_metrics_evaluation_model.accuracy,samb_metrics_evaluation_model.precisions,samb_metrics_evaluation_model.recall,samb_metrics_evaluation_model.f1_score,samb_metrics_evaluation_model.registration_date,samb_metrics_evaluation_model.update_date,samb_metrics_evaluation_model.state)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[data['id'],data['type_model'],self.generate_string(data['accuracy']),self.generate_string(data['precision']),self.generate_string(data['recall']),self.generate_string(data['f1']),data['registration_date'],data['update_date'],data['state']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_metrics_evaluation_model: '+str(err)}

        return {'status':True,'msj':'Success'}