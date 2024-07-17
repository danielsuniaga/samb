from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.framework.framework import cases_framework

class TestServicesDates(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_framework(self.mock_cursor)

    def test_get(self):

        result = self.service.get()
        
        self.assertTrue(result)

    @mock.patch('apis.repositories.framework.framework.repositories_framework.add')
    def test_add(self, mock_get):

        mock_get.return_value = {'status':True,'msj':'Success'}

        result = self.service.add("TEST","22040102","TEST")

        self.assertEqual(result, {'status':True,'msj':'Success'})

    def test_generate_framework_id(self):

        cronjob_id = self.service.generate_id()

        self.assertIsInstance(cronjob_id, str)

        unique_ids = set()

        unique_ids.add(cronjob_id)

        for _ in range(1000):  

            new_id = self.service.generate_id()

            self.assertNotIn(new_id, unique_ids)

            unique_ids.add(new_id)
