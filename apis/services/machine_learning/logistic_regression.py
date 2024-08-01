import apis.repositories.machine_learning.logistic_regression as repository_logistic_regression

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix, ConfusionMatrixDisplay

import pandas as pd

import os

import matplotlib.pyplot as plt

import pickle

from decouple import config

class case_logistic_regression():

    dataset_file_general = None

    logistic_regression = None

    directory_file_general = None

    directory_model_general = None

    model_logistic_regression_general = None

    name_model_logistic_regression_general = None

    def __init__(self,cursor):

        self.logistic_regression = repository_logistic_regression.repositories_ligistic_regression(cursor)

    def init_directory_model_general(self):

        self.model_logistic_regression_general = config("DIRECTORY_GENERAL_MODEL_ML_LOGISTIC_REGRESSION")

        return True
    
    def init_name_model_logistic_regression_general(self):

        self.name_model_logistic_regression_general = config("MODEL_GENERAL_MODEL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_name_model_logistic_regression_general(self):

        return self.name_model_logistic_regression_general

    def get_directory_model_general(self):

        return self.model_logistic_regression_general

    def init_dataset_file_general(self):
        
        self.dataset_file_general = config("DATASET_FILE_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def init_directory_file_general(self):

        self.directory_file_general = config("DIRECTORY_FILE_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_directory_file_general(self):

        return self.directory_file_general
    
    def analize_directory_exists(self, directory):

        if not os.path.exists(directory):

            os.makedirs(directory)

            self.analize_directory_exists(directory)

        return True

    def get_dataset_file_general(self):

        return self.dataset_file_general
    
    def get_data_dataset_general(self):

        return self.logistic_regression.get_dataset_general()
    
    def generate_dataframe_with_data(self,data):

        return pd.DataFrame(data)
    
    def analized_dataset_file(self):

        return os.path.exists(self.get_dataset_file_general())
    
    def add_dataset_historic(self):

        self.init_dataset_file_general()

        self.init_directory_file_general()

        if not self.analize_directory_exists(self.get_directory_file_general()):

            return False

        result = self.get_data_dataset_general()

        if not result['status']:

            return False
        
        dataframe = self.generate_dataframe_with_data(result['data'])
        
        try:

            dataframe.to_csv(self.get_directory_file_general()+self.get_dataset_file_general(), index=False)
        
        except Exception as e:

            return False
                
        return True
    
    def get_status_dataframe(self,data):

        print(data.head())

        print(data.info())

        return True
    
    def load_data(self):

        dataset_path = self.get_directory_file_general() + self.get_dataset_file_general()

        data = pd.read_csv(dataset_path)
        
        if 'entry_registration_date' in data.columns:
            
            data['entry_registration_date'] = data['entry_registration_date'].astype(str)
            
            data['year'] = data['entry_registration_date'].str[:4].astype(int)
            
            data['month'] = data['entry_registration_date'].str[4:6].astype(int)

            data['day'] = data['entry_registration_date'].str[6:8].astype(int)

            data['hour'] = data['entry_registration_date'].str[8:10].astype(int)

            data['minute'] = data['entry_registration_date'].str[10:12].astype(int)

            data['second'] = data['entry_registration_date'].str[12:14].astype(int)
            
            data.drop(columns=['entry_registration_date'], inplace=True)
        
        return data
    
    def preprocess_data(self, data):

        X = data.drop(columns=['entry_result'])

        y = data['entry_result']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):

        self.model = LogisticRegression()

        self.model.fit(X_train, y_train)

        return self.model
    
    def generate_training(self):

        self.init_dataset_file_general()

        self.init_directory_file_general()
        
        data = self.load_data()

        print(data)

        return True

        X_train, X_test, y_train, y_test = self.preprocess_data(data)

        self.train_model(X_train, y_train)

        return True

        # accuracy, report, matrix = self.evaluate_model(X_test, y_test)

        # self.save_model()
        
        # return accuracy, report, matrix
    
    def load_model(self):
        model_path = os.path.join(self.get_directory_file_general(), 'logistic_regression_model.pkl')
        if os.path.exists(model_path):
            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)
            return self.model
        return None