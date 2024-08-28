from unittest import TestCase, mock

from apis.repositories.machine_learning.logistic_regression import repositories_ligistic_regression

class TestRepositoriesLogisticRegression(TestCase):

    mock_cursor = None

    repo = None

    def setUp(self):

        self.mock_cursor = mock.MagicMock()

        self.repo = repositories_ligistic_regression(self.mock_cursor)

    def test_get_sma10(self):

        experted_result= 4

        self.repo.sma10 = experted_result

        result = self.repo.get_sma10()

        self.assertEqual(result,experted_result)
        
    def test_get_sma30(self):

        experted_result= 4

        self.repo.sma30 = experted_result

        result = self.repo.get_sma30()

        self.assertEqual(result,experted_result)

    def test_get_rsi(self):

        experted_result= 4

        self.repo.rsi = experted_result

        result = self.repo.get_rsi()

        self.assertEqual(result,experted_result)
