import apis.repositories.machine_learning.logistic_regression as repository_logistic_regression

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report

import pandas as pd

import os

from decouple import config

class case_logistic_regression():

    dataset_file_general = None

    logistic_regression = None

    directory_file_general = None

    model_logistic_regression_general = None

    def __init__(self,cursor):

        self.logistic_regression = repository_logistic_regression.repositories_ligistic_regression(cursor)

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
    
    def train_model(self):

        self.init_dataset_file_general()

        self.init_directory_file_general()

        dataset_path = self.get_directory_file_general() + self.get_dataset_file_general()

        if not self.analize_directory_exists(dataset_path):

            return False
               
        data = pd.read_csv(dataset_path)

        self.get_status_dataframe(data)

        return True
        
        # Separar características y etiqueta
        X = data.drop(columns=['entry_result'])
        y = data['entry_result']
        
        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Entrenar el modelo
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)
        
        # Hacer predicciones y evaluar el modelo
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        # Guardar el modelo en un archivo
        with open(os.path.join(self.get_directory_file_general(), 'logistic_regression_model.pkl'), 'wb') as model_file:
            pickle.dump(self.model, model_file)
        
        return self.model, accuracy, report
    
    def load_model(self):
        model_path = os.path.join(self.get_directory_file_general(), 'logistic_regression_model.pkl')
        if os.path.exists(model_path):
            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)
            return self.model
        return None