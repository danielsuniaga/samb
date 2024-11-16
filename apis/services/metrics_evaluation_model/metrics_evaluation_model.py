import apis.repositories.metrics_evaluation_model.metrics_evaluation_model as repositories_metrics_evaluation_model

from apis.services.metrics_evaluation_model.imetrics_evaluation_model import icase_metrics_evaluation_model
class case_metrics_evaluation_model(icase_metrics_evaluation_model):

    models = None

    state_default = None

    metrics_evaluation_model = None

    accuracy = None

    precision = None

    recall = None

    f1 = None

    def __init__(self,cursor):
       
       self.metrics_evaluation_model = repositories_metrics_evaluation_model.repositories_metrics_evaluation_model(cursor)
       
       self.init_models()

       self.init_state_default()

    def get_accuracy(self):

        return self.accuracy
    
    def set_accuracy(self,value):

        self.accuracy = value

        return True
    
    def get_precision(self):

        return self.precision
    
    def set_precision(self,value):

        self.precision = value

        return True
    
    def get_recall(self):

        return self.recall 
    
    def set_recall(self,value):

        self.recall = value

        return True
    
    def get_f1(self):

        return self.f1 
    
    def set_f1(self,value):

        self.f1 = value

        return True

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

        self.set_accuracy(data['accuracy'])

        self.set_precision(data['precision'])

        self.set_f1(data['f1'])

        self.set_recall(data['recall'])

        result = self.metrics_evaluation_model.add(data)

        return True