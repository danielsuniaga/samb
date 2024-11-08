class repositories_metrics_evaluation_model():

    cursor_db = None

    def __init__(self,cursor):

        self.cursor_db = cursor

    def add(self,data):

        try:

            self.cursor_db.execute("INSERT INTO samb_entry_predict_model_general_logistic_regression(samb_entry_predict_model_general_logistic_regression.id,samb_entry_predict_model_general_logistic_regression.id_entry,samb_entry_predict_model_general_logistic_regression.id_predict_model_general_logistic_regression,samb_entry_predict_model_general_logistic_regression.registration_date,samb_entry_predict_model_general_logistic_regression.update_date,samb_entry_predict_model_general_logistic_regression.state)VALUES(%s,%s,%s,%s,%s,%s)",[data['id'],data['id_entry'],data['id_predict_model_general_logistic_regression'],data['registration_date'],data['update_date'],data['state']])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entry_predict_model_general_logistic_regression: '+str(err)}

        return {'status':True,'msj':'Success'}