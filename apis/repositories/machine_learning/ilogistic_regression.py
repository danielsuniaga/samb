from abc import ABC, abstractmethod

class irepositories_ligistic_regression(ABC):

    @abstractmethod
    def get_sma10(self):
        pass

    @abstractmethod
    def get_sma30(self):
        pass

    @abstractmethod
    def get_rsi(self):
        pass

    @abstractmethod
    def get_dataset_general_expansive(self):
        pass

    @abstractmethod
    def get_dataset_general(self):
        pass

    @abstractmethod
    def add_models_general(self,data):
        pass

    @abstractmethod
    def add_entry_model_general(self,data):
        pass