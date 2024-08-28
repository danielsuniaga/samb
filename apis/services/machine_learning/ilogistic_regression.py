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
    def get_status_dataframe(self,data):
        pass

    @abstractmethod
    def load_data_expansive(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def preprocess_data(self,data):
        pass

    @abstractmethod
    def preprocess_data_expansive(self,X,y):
        pass

    @abstractmethod
    def train_model(self, X_train, y_train):
        pass

    @abstractmethod
    def evaluate_model(self, X_test, y_test):
        pass

    @abstractmethod
    def get_model_general_path(self):
        pass

    @abstractmethod
    def save_model(self):
        pass

    @abstractmethod
    def generate_training(self):
        pass

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def get_path_flat_data_model_general(self):
        pass

    @abstractmethod
    def add_flat_data_model_general(self,data):
        pass

    @abstractmethod
    def generate_position_prediction(self,data):
        pass

    @abstractmethod
    def generate_id(self):
        pass

    @abstractmethod
    def get_current_utc5(self):
        pass

    @abstractmethod
    def get_current_date(self):
        pass

    @abstractmethod
    def get_current_date_only(self):
        pass

    @abstractmethod
    def get_current_date_mil(self):
        pass

    @abstractmethod
    def init_data_predictions(self,result,result_general):
        pass

    @abstractmethod
    def generate_date_to_str(self,field):
        pass

    @abstractmethod
    def get_stage_prediction_field_front(self,field):
        pass

    @abstractmethod
    def set_message_user_predictions(self,predictions):
        pass

    @abstractmethod
    def init_data_persistent_model_general(self,data):
        pass

    @abstractmethod
    def get_position_prediction(self,data):
        pass

    @abstractmethod
    def init_add_entry_predict_model_general_logistic_regression(self,id_predict,id_entry):
        pass

    @abstractmethod
    def add_entry_predict_model_general_logistic_regression(self,id_predict,id_entry):
        pass