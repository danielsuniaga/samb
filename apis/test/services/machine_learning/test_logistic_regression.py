from unittest import TestCase, mock

from unittest.mock import patch

import unittest

from apis.services.metrics_evaluation_model.metrics_evaluation_model import case_metrics_evaluation_model

from apis.services.machine_learning.logistic_regression import case_logistic_regression

from apis.services.telegram.telegram import cases_telegram

from decimal import Decimal

from django.db import connection

import apis.services.dates.dates as case_dates

class TestServiceaMachineLearningLogisticRegression(TestCase):

    mock_cursor = None

    service = None
    
    service_real = None

    services_real_metrics_evaluation_model = None

    services_date = None

    cursor = None
    
    def setUp(self):

        self.mock_cursor = mock.MagicMock()

        self.cursor = connection.cursor()

        self.services_date = case_dates.cases_dates()

        self.service = case_logistic_regression(self.mock_cursor)

        self.services_real_metrics_evaluation_model = case_metrics_evaluation_model(self.cursor)

        self.service_real = case_logistic_regression(self.cursor)

        self.service_real.init_object_date(self.services_date)

        self.service_real.init_object_object_metrics_evaluation_model(self.services_real_metrics_evaluation_model)

    def test_check_active_general(self):

        result = self.service.check_active_general()

        print(result)
    
    def test_init_extension_data_model_general(self):

        result = self.service.init_extension_data_model_general()

        self.assertTrue(result)

    def test_init_data_model_general(self):

        result = self.service.init_data_model_general()

        self.assertTrue(result)

    def test_init_data_directory_model_general(self):

        result = self.service.init_data_directory_model_general()

        self.assertTrue(result)

    @unittest.skip("Skipping this test")
    def test_add_dataset_historic(self):

        result = self.service_real.add_dataset_historic()

        self.assertTrue(result)

    
    # @unittest.skip("Skipping this test")
    def test_generate_training(self):

        dates = case_dates.cases_dates()

        telegram = cases_telegram(self.cursor)

        self.service_real.init_object_date(dates)

        self.service_real.init_object_telegram(telegram)

        result = self.service_real.generate_training()

        print(result)

    @unittest.skip("Skipping this test")
    def test_get_position_prediction(self):

        dates = case_dates.cases_dates()

        data = {
            "entry_type": 1,
            "entry_type_account": 2,
            "entry_number_candle": 10,
            "entry_condition": 0,
            "entry_amount": 1,
            "sma_30_value": 50.5,
            "sma_10_value": 45.3,
            "rsi_value": 70.0,
            "movement_open_candle": 1.1,
            "movement_close_candle": 1.2,
            "movement_high_candle": 1.3,
            "movement_low_candle": 1.0,
            "movement_volume_candle": 100,
            "year": 2024,
            "month": 8,
            "day": 10,
            "hour": 14,
            "minute": 30,
            "second": 15
        }

        self.service_real.init_object_date(dates)

        result = self.service_real.get_position_prediction(data)

        print(result)

    @unittest.skip("Skipping this test")
    def test_add_flat_data_model_general(self):

        data="TEST"

        dates = case_dates.cases_dates()

        self.service_real.init_object_date(dates)

        result = self.service_real.add_flat_data_model_general(data)

        print(result)

    def test_add_metrics_evaluation_model(self):

        accuracy = 0.56

        precision = 0.53

        recall = 0.86

        f1 = 0.66

        result = self.service_real.add_metrics_evaluation_model(accuracy,precision,recall,f1)

        print(result)



