from abc import ABC, abstractmethod

class icase_metrics_evaluation_model(ABC):

    @abstractmethod
    def init_state_default(self):
        pass

    @abstractmethod
    def get_state_default(self):
        pass

    @abstractmethod
    def init_models(self):
        pass

    @abstractmethod
    def get_models_general_logistic(self):
        pass

    @abstractmethod
    def add(self,data):
        pass