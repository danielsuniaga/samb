from abc import ABC, abstractmethod

class icase_logistic_regression(ABC):

    @abstractmethod
    def init_extension_data_model_general(self):
        pass

    @abstractmethod
    def get_extension_data_model_general(self):
        pass

    @abstractmethod
    def init_data_model_general(self):
        pass

    @abstractmethod
    def add_data_model_general(self,value):
        pass

    @abstractmethod
    def get_data_model_general(self):
        pass

    @abstractmethod
    def init_data_directory_model_general(self):
        pass

    @abstractmethod
    def get_data_directory_model_general(self):
        pass

    @abstractmethod
    def set_message_user(self,value):
        pass

    @abstractmethod
    def get_message_user(self):
        pass

    @abstractmethod
    def set_id_predict_model_general_repository(self,value):
        pass

    @abstractmethod
    def get_id_predict_model_general_repository(self):
        pass

    @abstractmethod
    def init_object_date(self,value):
        pass

    @abstractmethod
    def init_stage_prediction(self):
        pass

    @abstractmethod
    def get_stage_prediction_field(self,field):
        pass

    @abstractmethod
    def set_stage_prediction_field(self,field,value):
        pass

    @abstractmethod
    def init_model_general(self):
        pass

    @abstractmethod
    def get_model_general(self):
        pass

    @abstractmethod
    def init_model_general(self):
        pass

    @abstractmethod
    def init_directory_model_general(self):
        pass

    @abstractmethod
    def get_directory_model_general(self):
        pass

    @abstractmethod
    def init_matriz_general(self):
        pass

    @abstractmethod
    def get_matriz_general(self):
        pass

    @abstractmethod
    def init_matriz_general(self):
        pass

    @abstractmethod
    def init_matriz_directory_general(self):
        pass

    @abstractmethod
    def init_dataset_file_general(self):
        pass

    @abstractmethod
    def init_directory_file_general(self):
        pass

    @abstractmethod
    def init_dataset_file_general(self):
        pass

    @abstractmethod
    def get_directory_file_general(self):
        pass

    @abstractmethod
    def get_dataset_file_general(self):
        pass

    @abstractmethod
    def analize_directory_exists(self,directory):
        pass

    @abstractmethod
    def get_data_dataset_general(self):
        pass

    @abstractmethod
    def generate_dataframe_with_data(self,data):
        pass

    @abstractmethod
    def analized_dataset_file(self):
        pass

    @abstractmethod
    def add_dataset_historic(self):
        pass

    @abstractmethod
    def analize_directory_exists(self,directory):
        pass