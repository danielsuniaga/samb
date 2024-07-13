from unittest import TestCase, mock

from apis.services.api.api import cases_api

from decouple import config

class TestServicesApi(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_api(self.mock_cursor)

        self.api_key = config("API")

    @mock.patch('apis.repositories.api.repositories_api.get')
    def test_get_api_result(self, mock_get):

        mock_get.return_value = "TEST"

        result = self.service.get_api_result()

        self.assertEqual(result, "TEST")

    @mock.patch('apis.repositories.api.repositories_api.get_api_key')
    def test_get_api_key_with_key_present(self,mock_get):

        expected_result = {'status': True, 'msj': 'Success'}
        
        mock_request = mock.MagicMock()

        mock_request.headers = {self.api_key: "test_value"}
        
        mock_get.return_value = expected_result
        
        result = self.service.get_api_key(mock_request)

        self.assertEqual(result, expected_result)