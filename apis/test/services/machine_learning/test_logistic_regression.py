from unittest import TestCase, mock

from unittest.mock import patch

from decimal import Decimal

from django.db import connection

from apis.services.machine_learning.logistic_regression import case_logistic_regression

class TestServiceaMachineLearningLogisticRegression(TestCase):

    mock_cursor = None

    service = None

    service_real = None

    cursor = None
    
    def setUp(self):

        self.mock_cursor = mock.MagicMock()

        self.cursor = connection.cursor()

        self.service = case_logistic_regression(self.mock_cursor)

        self.service_real = case_logistic_regression(self.cursor)

    def test_add_dataset_historic(self):

        result = self.service_real.add_dataset_historic()

        self.assertTrue(result)

    def test_train_model(self):

        result = self.service_real.train_model()
        

