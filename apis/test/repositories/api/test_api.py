from unittest import TestCase, mock

from apis.repositories.api.api import repositories_api

class TestRepositoriesApi(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_api(self.mock_cursor)

    def test_get_success(self):

        self.mock_cursor.execute.return_value = 1

        result = self.repo.get()

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_get_api_key_success(self):

        self.mock_cursor.execute.return_value = 1

        key="TEST"

        value ="TEST"

        result = self.repo.get_api_key(key,value)

        self.assertEqual(result, {'status': True, 'msj': 'Success'})