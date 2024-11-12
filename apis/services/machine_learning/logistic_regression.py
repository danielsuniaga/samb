import apis.repositories.machine_learning.logistic_regression as repository_logistic_regression

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix, ConfusionMatrixDisplay,precision_score,recall_score,f1_score

import pandas as pd

import os

import matplotlib.pyplot as plt

import pickle

import uuid

from decouple import config

import time

from apis.services.machine_learning.ilogistic_regression import icase_logistic_regression

class case_logistic_regression(icase_logistic_regression):

    active_general = None

    dataset_file_general = None

    matriz_general = None

    directory_file_general = None

    matriz_directory_general = None

    logistic_regression = None

    model_general = None

    directory_model_general = None

    data_model_general = None

    data_directory_model_general = None

    extension_data_model_general = None

    model = None

    object_date = None

    stage_prediction = None

    id_predict_model_general_repository = None

    message_user = None

    object_telegram = None

    project_name = None

    message_default_services = None

    object_metrics_evaluation_model = None

    def __init__(self,cursor):

        self.logistic_regression = repository_logistic_regression.repositories_ligistic_regression(cursor)

        self.project_name = config("PROJECT_NAME")

        self.init_active_general()
    
        self.init_messsage_default_services()

    def init_object_object_metrics_evaluation_model(self,value):

        self.object_metrics_evaluation_model = value

        return True
    
    def init_messsage_default_services(self):

        self.message_default_services = " MODEL GENERAL DEACTIVATE "

        return True
    
    def get_message_default_services(self):

        return self.message_default_services

    def init_active_general(self):

        self.active_general = int(config("ACTIVE_GENERAL_ML_LOGISTIC_REGRESSION"))

        return True
    
    def get_active_general(self):

        return self.active_general
    
    def check_active_general(self):

        if not self.get_active_general():

            return False

        return True
    
    def get_project_name(self):
        
        return self.project_name

    def init_object_telegram(self,value):

        self.object_telegram = value

        return True
    
    def init_extension_data_model_general(self):
        
        self.extension_data_model_general = config("MODEL_GENERAL_DATA_EXTENSION_ML_LOGISTIC_REGRESSION")

        return True
    
    def get_extension_data_model_general(self):

        return self.extension_data_model_general
    
    def init_data_model_general(self):

        self.data_model_general = config("MODEL_GENERAL_DATA_ML_LOGISTIC_REGRESSION")

        return True

    def add_data_model_general(self,value):

        self.data_model_general = self.data_model_general + value
    
    def get_data_model_general(self):

        return self.data_model_general
    
    def init_data_directory_model_general(self):

        self.data_directory_model_general = config("MODEL_DIRECTORY_DATA_ML_LOGISTIC_REGRESSION")

        return True

    def get_data_directory_model_general(self):

        return self.data_directory_model_general
    
    def set_message_user(self,value):

        self.message_user = value

        return True;

    def get_message_user(self):

        return self.message_user
    
    def set_id_predict_model_general_repository(self,value):

        self.id_predict_model_general_repository = value

        return True
    
    def get_id_predict_model_general_repository(self):

        return self.id_predict_model_general_repository
    
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
    
    def add_matriz_general(self,value):

        self.matriz_general = value + self.matriz_general

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

        if not self.check_active_general():

            return True

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

        data = pd.read_csv(self.get_directory_file_general() + self.get_dataset_file_general())

        processed_data = pd.DataFrame()

        grouped = data.groupby('id_entry_id')

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

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):

        self.model = LogisticRegression(max_iter=500)

        self.model.fit(X_train, y_train)

        return self.model
    
    def get_models_general_logistics(self):

        return self.object_metrics_evaluation_model.get_models_general_logistic()
    
    def get_models_metrics_states_default(self):

        return self.object_metrics_evaluation_model.get_state_default()

    def init_data_add_metrics_evaluation_model(self,accuracy,precision,recall,f1):

        date = self.get_current_date()

        return {
            
            "id":self.generate_id(),
            "type_model":self.get_models_general_logistics(),
            "accuracy":accuracy,
            "precision":precision,
            "recall":recall,
            "f1":f1,
            "registration_date":date,
            "update_date":date,
            "state":self.get_models_metrics_states_default()

        }
    
    def add_metrics_evaluation_model(self,accuracy,precision,recall,f1):

        data = self.init_data_add_metrics_evaluation_model(accuracy,precision,recall,f1)

        return self.object_metrics_evaluation_model.add(data)
    
    def evaluate_model(self, X_test, y_test):

        self.init_matriz_directory_general()

        self.init_matriz_general()

        self.add_matriz_general(self.get_current_date_only()+" - ")

        y_pred = self.model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        
        report = classification_report(y_test, y_pred, zero_division=0)

        precision = precision_score(y_test, y_pred)

        recall = recall_score(y_test, y_pred)

        f1 = f1_score(y_test, y_pred)

        self.add_metrics_evaluation_model(accuracy,precision,recall,f1)
        
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

            # print(f"Modelo guardado correctamente en: {model_path}")

        except Exception as e:

            # print(f"Error al guardar el modelo: {str(e)}")

            return False
        
        return True
    
    def generate_msj_notification(self):

        return "General model logistic progression training Project: "+self.get_project_name()
    
    def send_msj_telegram_without_persistence(self,msj):

        return self.object_telegram.send_without_persistence(msj)
    
    def generate_training(self):

        if not self.check_active_general():

            return True

        self.init_dataset_file_general()

        self.init_directory_file_general()
        
        data = self.load_data()  

        X_train, X_test, y_train, y_test = self.preprocess_data(data)
        
        self.train_model(X_train, y_train)
        
        accuracy, report = self.evaluate_model(X_test, y_test)

        self.save_model()

        self.send_msj_telegram_without_persistence(self.generate_msj_notification())
        
        return True
    
    def load_model(self):

        model_path = self.get_model_general_path()

        if os.path.exists(model_path):
            
            with open(model_path, 'rb') as model_file:
               
                self.model = pickle.load(model_file)
            
            return self.model
        
        return None
    
    def get_path_flat_data_model_general(self):
        
        return self.get_data_directory_model_general()+self.get_data_model_general()+self.get_extension_data_model_general()
    
    def add_flat_data_model_general(self,data):

        self.init_data_model_general()

        self.add_data_model_general(self.get_current_date_only())

        self.init_data_directory_model_general()

        self.init_extension_data_model_general()

        self.analize_directory_exists(self.get_data_directory_model_general())

        path = self.get_path_flat_data_model_general()

        try:

            with open(path, 'a') as archivo:  

                archivo.write(str(data) + '\n')

        except Exception as e:

            return False
        
        return True
    
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
    
    def get_current_date_only(self):

        now = self.get_current_utc5()
        
        return self.object_date.get_current_date_only(now)
    
    def get_current_date_mil(self):

        now = self.get_current_utc5()

        return self.object_date.get_current_date_mil(now)
    
    def init_data_predictions(self,result,result_general):

        return {"general":result_general[0],"false":result[0][0],"true":result[0][1]}
    
    def generate_date_to_str(self,field):
        
        return self.object_date.generate_date_to_str(field)
    
    def get_stage_prediction_field_front(self,field):

        date = self.generate_date_to_str(self.get_stage_prediction_field(field))

        return self.object_date.get_current_date_mil_front(date)
    
    def set_message_user_predictions(self,predictions):

        self.set_message_user(" - [Prediction general: "+str(predictions['general'])+" Prediction false: "+str(predictions['false'])+" Prediction true: "+str(predictions['true'])+"] - [Start date:"+self.get_stage_prediction_field_front("start")+" Load date:"+self.get_stage_prediction_field_front("load")+" Predict general date:"+self.get_stage_prediction_field_front("predict_general")+" Predict proba date:"+self.get_stage_prediction_field_front("predict_proba")+"]")

        return True
    
    def init_data_persistent_model_general(self,data):

        self.init_stage_prediction()

        date = self.get_current_date()

        self.add_flat_data_model_general(data)

        result,result_general = self.generate_position_prediction(data)

        predictions = self.init_data_predictions(result,result_general)

        self.set_id_predict_model_general_repository(self.generate_id())

        self.set_message_user_predictions(predictions)

        return {
            "id": self.get_id_predict_model_general_repository(),
            "predition_general":predictions['general'],
            "prediction_false": predictions['false'],
            "prediction_true": predictions['true'],
            "start_date": self.get_stage_prediction_field("start"),
            "load_date": self.get_stage_prediction_field("load"),
            "predict_general_date": self.get_stage_prediction_field("predict_general"),
            "predict_proba_date": self.get_stage_prediction_field("predict_proba"),
            "registration_date": date,
            "update_date": date,
            "state": 1
        }

    def get_position_prediction(self,data):

        result = self.logistic_regression.add_models_general(self.init_data_persistent_model_general(data))
        
        if not result['status']:

            return False
        
        print(self.get_message_user())

        return self.get_id_predict_model_general_repository()
    
    def init_add_entry_predict_model_general_logistic_regression(self,id_predict,id_entry):

        date = self.get_current_date()

        return {
            "id": self.generate_id(),
            "id_entry":id_entry,
            "id_predict_model_general_logistic_regression":id_predict,
            "registration_date":date,
            "update_date":date,
            "state":1
        }
    
    def add_entry_predict_model_general_logistic_regression(self,id_predict,id_entry):

        result = self.logistic_regression.add_entry_model_general(self.init_add_entry_predict_model_general_logistic_regression(id_predict,id_entry))

        if not result['status']: 

            return False

        return True