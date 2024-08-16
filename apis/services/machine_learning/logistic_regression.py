import apis.repositories.machine_learning.logistic_regression as repository_logistic_regression

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix, ConfusionMatrixDisplay

import pandas as pd

import os

import matplotlib.pyplot as plt

import pickle

import uuid

from decouple import config

import time

class case_logistic_regression():

    dataset_file_general = None

    matriz_general = None

    directory_file_general = None

    matriz_directory_general = None

    logistic_regression = None

    model_general = None

    directory_model_general = None

    model = None

    object_date = None

    stage_prediction = None

    def __init__(self,cursor):

        self.logistic_regression = repository_logistic_regression.repositories_ligistic_regression(cursor)

    def init_object_date(self,value):

        self.object_date = value

        return True
    
    def init_stage_prediction(self):

        self.stage_prediction = {
            "start": "",
            "load": "",
            "predict_general": "",
            "predict_proba":""
        }

        return True
    
    def get_stage_prediction_field(self,field):

        return self.stage_prediction[field]
    
    def set_stage_prediction_field(self,field,value):

        self.stage_prediction[field] = value

        return True
   
    def init_model_general(self):

        self.model_general = config("MODEL_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_model_general(self):

        return self.model_general
    
    def init_directory_model_general(self):

        self.directory_model_general = config("MODEL_DIRECTORY_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_directory_model_general(self):

        return self.directory_model_general

    def init_matriz_general(self):

        self.matriz_general = config("MATRIZ_GENERAL_ML_LOGISTIC_REGRESSION")

        return True

    def get_matriz_general(self):

        return self.matriz_general
    
    def init_matriz_directory_general(self):

        self.matriz_directory_general = config("MATRIZ_DIRECTORY_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_matriz_directory_general(self):

        return self.matriz_directory_general
    
    def init_dataset_file_general(self):
        
        self.dataset_file_general = config("DATASET_FILE_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def init_directory_file_general(self):

        self.directory_file_general = config("DIRECTORY_FILE_GENERAL_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_directory_file_general(self):

        return self.directory_file_general
    
    def get_dataset_file_general(self):

        return self.dataset_file_general
    
    def analize_directory_exists(self, directory):

        if not os.path.exists(directory):

            os.makedirs(directory)

            self.analize_directory_exists(directory)

        return True
    
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

        print("HEAD-----------------------------")

        print(data.head())

        print("INFO-----------------------------")

        print(data.info())

        return True
    
    def load_data_expansive(self):

        # Leer los datos desde el archivo CSV
        data = pd.read_csv(self.get_directory_file_general() + self.get_dataset_file_general())

        # Crear un nuevo DataFrame para almacenar las posiciones con las velas embebidas
        processed_data = pd.DataFrame()

        # Agrupar por cada posición y ordenar por num_candle para mantener las últimas 30 velas
        grouped = data.groupby('id_entry_id')

        # Iterar sobre cada grupo (posición)
        for name, group in grouped:

            # Crear un diccionario para la nueva fila
            row = {
                'entry_type': group.iloc[0]['entry_type'],
                'entry_type_account': group.iloc[0]['entry_type_account'],
                'entry_number_candle': group.iloc[0]['entry_number_candle'],
                'entry_condition': group.iloc[0]['entry_condition'],
                'entry_amount': group.iloc[0]['entry_amount'],
                'entry_registration_date': group.iloc[0]['entry_registration_date'],
                'sma_30_value': group.iloc[0]['sma_30_value'],
                'sma_10_value': group.iloc[0]['sma_10_value'],
                'rsi_value': group.iloc[0]['rsi_value'],
                'entry_result': group.iloc[0]['entry_result']
            }

            # Añadir las 30 últimas velas
            for i in range(30):
                prefix = f'movement_{i+1}'

                if i < len(group):
                    row[f'{prefix}_open_candle'] = group.iloc[i]['movement_open_candle']
                    row[f'{prefix}_close_candle'] = group.iloc[i]['movement_close_candle']
                    row[f'{prefix}_high_candle'] = group.iloc[i]['movement_high_candle']
                    row[f'{prefix}_low_candle'] = group.iloc[i]['movement_low_candle']
                    row[f'{prefix}_volume_candle'] = group.iloc[i]['movement_volume_candle']
                else:
                    row[f'{prefix}_open_candle'] = None
                    row[f'{prefix}_close_candle'] = None
                    row[f'{prefix}_high_candle'] = None
                    row[f'{prefix}_low_candle'] = None
                    row[f'{prefix}_volume_candle'] = None

            # Añadir la fila al DataFrame procesado
            processed_data = pd.concat([processed_data, pd.DataFrame([row])], ignore_index=True)

        # Separar características y objetivo
        X = processed_data.drop(columns=['entry_result'])
        y = processed_data['entry_result']

        return X, y

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

        data.drop(columns=['id_entry_id'], inplace=True)
        
        return data
    
    def preprocess_data(self, data):

        X = data.drop(columns=['entry_result'])

        y = data['entry_result']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def preprocess_data_expansive(self, X, y):

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):

        self.model = LogisticRegression(max_iter=500)

        self.model.fit(X_train, y_train)

        return self.model

    def evaluate_model(self, X_test, y_test):

        self.init_matriz_directory_general()

        self.init_matriz_general()

        y_pred = self.model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        
        report = classification_report(y_test, y_pred, zero_division=0)
        
        cm = confusion_matrix(y_test, y_pred)

        cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        
        fig, ax = plt.subplots(figsize=(10, 7))

        cm_display.plot(cmap=plt.cm.Blues, ax=ax)

        if self.analize_directory_exists(self.get_matriz_directory_general()):

            plt.savefig(self.get_matriz_directory_general()+self.get_matriz_general())
                
        return accuracy, report

    def get_model_general_path(self):

        return self.get_directory_model_general()+self.get_model_general()

    def save_model(self):

        self.init_model_general()

        self.init_directory_model_general()

        if not self.analize_directory_exists(self.get_directory_model_general()):

            return False

        model_path = self.get_model_general_path()
    
        try:

            with open(model_path, 'wb') as model_file:

                pickle.dump(self.model, model_file)

            print(f"Modelo guardado correctamente en: {model_path}")

        except Exception as e:

            print(f"Error al guardar el modelo: {str(e)}")

            return False
        
        return True
    
    def generate_training(self):

        self.init_dataset_file_general()

        self.init_directory_file_general()
        
        data = self.load_data()  

        X_train, X_test, y_train, y_test = self.preprocess_data(data)
        
        self.train_model(X_train, y_train)
        
        accuracy, report= self.evaluate_model(X_test, y_test)

        self.save_model()
        
        return True
    
    def load_model(self):

        model_path = self.get_model_general_path()

        if os.path.exists(model_path):
            
            with open(model_path, 'rb') as model_file:
               
                self.model = pickle.load(model_file)
            
            return self.model
        
        return None
    
    def generate_position_prediction(self,data):

        self.set_stage_prediction_field("start",self.get_current_date_mil())

        df = pd.DataFrame([data])

        self.init_model_general()

        self.init_directory_model_general()

        if not self.analize_directory_exists(self.get_directory_model_general()):

            return False
        
        model = self.load_model()

        self.set_stage_prediction_field("load",self.get_current_date_mil())

        prediction = model.predict_proba(df)

        self.set_stage_prediction_field("predict_general",self.get_current_date_mil())

        predition_general = model.predict(df)

        self.set_stage_prediction_field("predict_proba",self.get_current_date_mil())

        return prediction, predition_general
    
    def generate_id(self):

        return uuid.uuid4().hex
    
    def get_current_utc5(self):

        return self.object_date.get_current_utc5()
    
    def get_current_date(self):

        now = self.get_current_utc5()
        
        return self.object_date.get_current_date(now)
    
    def get_current_date_mil(self):

        now = self.get_current_utc5()

        return self.object_date.get_current_date_mil(now)
    
    def init_data_persistent_model_general(self,data,id_entry):

        self.init_stage_prediction()

        date = self.get_current_date()

        result,result_general = self.generate_position_prediction(data)

        return {
            "id": self.generate_id(),
            "id_entrys": id_entry,
            "predition_general":result_general[0],
            "prediction_false": result[0][0],
            "prediction_true": result[0][1],
            "start_date": self.get_stage_prediction_field("start"),
            "load_date": self.get_stage_prediction_field("load"),
            "predict_general_date": self.get_stage_prediction_field("predict_general"),
            "predict_proba_date": self.get_stage_prediction_field("predict_proba"),
            "registration_date": date,
            "update_date": date,
            "state": 1
        }

    def get_position_prediction(self,data,id_entry):

        result = self.init_data_persistent_model_general(data,id_entry)

        return self.logistic_regression.add_models_general(result)
