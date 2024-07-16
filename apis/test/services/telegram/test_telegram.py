from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.telegram.telegram import cases_telegram

import json

class TestServicesTelegram(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_telegram(self.mock_cursor)

    @mock.patch('apis.repositories.notification.notification.repositories_telegram.add')
    def test_send_reporting_email(self, mock_get):

        mock_get.return_value = {'status':True,'msj':'Success'} 

        result = self.service.send("TEST","1","20240606")

        self.assertEqual(result, {'status':True,'msj':'Success'})

    def test_translate_dictionary_json(self):

        test_dict = {"key1": "value1", "key2": 2, "key3": [1, 2, 3]}
        
        expected_result = json.dumps(test_dict)

        result = self.service.translate_dictionary_json(test_dict)

        self.assertEqual(result, expected_result)