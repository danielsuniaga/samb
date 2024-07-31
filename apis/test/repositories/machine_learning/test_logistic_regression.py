from unittest import TestCase, mock

from django.db import connection

from apis.repositories.machine_learning.logistic_regression import repositories_ligistic_regression

class TestRepositoriesLogisticRegression(TestCase):

    mock_cursor = None

    cursor = None

    repo = None

    def setUp(self):

        self.mock_cursor = mock.MagicMock()

        self.cursor = connection.cursor()

        self.repo = repositories_ligistic_regression(self.mock_cursor)

        self.repo_real = repositories_ligistic_regression(self.cursor)

    def test_get_dataset_general(self):

        result = self.repo_real.get_dataset_general()

        print(result)
        
