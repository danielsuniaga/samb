from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.machine_learning.logistic_regression import case_logistic_regression

class TestServiceaMachineLearningLogisticRegression(TestCase):

    mock_cursor = None

    service = None
    
    def setUp(self):

        self.mock_cursor = mock.MagicMock()

        self.service = case_logistic_regression(self.mock_cursor)

    def test_init_extension_data_model_general(self):

        result = self.service.init_extension_data_model_general()

        self.assertTrue(result)

    def test_init_data_model_general(self):

        result = self.service.init_data_model_general()

        self.assertTrue(result)

    def test_init_data_directory_model_general(self):

        result = self.service.init_data_directory_model_general()

        self.assertTrue(result)
