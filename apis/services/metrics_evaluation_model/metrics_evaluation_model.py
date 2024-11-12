import apis.repositories.metrics_evaluation_model.metrics_evaluation_model as repositories_metrics_evaluation_model

from apis.services.metrics_evaluation_model.imetrics_evaluation_model import icase_metrics_evaluation_model
class case_metrics_evaluation_model(icase_metrics_evaluation_model):

    models = None

    state_default = None

    metrics_evaluation_model = None

    def __init__(self,cursor):
       
       self.metrics_evaluation_model = repositories_metrics_evaluation_model.repositories_metrics_evaluation_model(cursor)
       
       self.init_models()

       self.init_state_default()

    def init_state_default(self):

        self.state_default = 1

        return True
    
    def get_state_default(self):

        return self.state_default

    def init_models(self):
       
       self.models = {
           
           'general_logistic' : 'GL'

       }

       return True

    def get_models_general_logistic(self):

        return self.models['general_logistic']

    def add(self,data):

        result = self.metrics_evaluation_model.add(data)

        return True