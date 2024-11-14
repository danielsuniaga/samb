from django.db import connection

import apis.services.dates.dates as case_dates

import apis.services.telegram.telegram as case_telegram

import apis.services.machine_learning.logistic_regression as case_logistic_regression

import apis.services.metrics_evaluation_model.metrics_evaluation_model as case_metrics_evaluation_model

class controller_add_model_regression_logistic():

    cursor = None

    date = None

    telegram  = None

    logistic_regression = None

    metrics_evaluation_model = None

    def __init__(self):

        cursor = connection.cursor()

        self.dates = case_dates.cases_dates()

        self.telegram = case_telegram.cases_telegram(cursor)

        self.logistic_regression = case_logistic_regression.case_logistic_regression(cursor)

        self.metrics_evaluation_model = case_metrics_evaluation_model.case_metrics_evaluation_model(cursor)

        self.logistic_regression.init_object_date(self.dates)
        
        self.logistic_regression.init_object_telegram(self.telegram)

        self.logistic_regression.init_object_object_metrics_evaluation_model(self.metrics_evaluation_model)

    def add_model_regression_logistic(self):

        if not self.logistic_regression.add_dataset_historic():

            return False
                
        return self.logistic_regression.generate_training()