from unittest import TestCase, mock

from apis.services.cronjobs.cronjobs import cases_cronjobs

class TestServicesCronjobs(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_cronjobs(self.mock_cursor)

    def test_generate_cronjob_id(self):

        cronjob_id = self.service.generate_cronjob_id()

        self.assertIsInstance(cronjob_id, str)

        unique_ids = set()

        unique_ids.add(cronjob_id)

        for _ in range(1000):  

            new_id = self.service.generate_cronjob_id()

            self.assertNotIn(new_id, unique_ids)

            unique_ids.add(new_id)

    @mock.patch('apis.repositories.cronjobs.repositories_cronjobs.add')
    def test_add(self, mock_get):

        mock_get.return_value = {'status':True,'msj':'Success'}

        result = self.service.add("TEST","22040102")

        self.assertEqual(result, {'status':True,'msj':'Success'})

    @mock.patch('apis.repositories.cronjobs.repositories_cronjobs.set_fields')
    def test_set_fields(self, mock_get):

        mock_get.return_value = {'status':True,'msj':'Success'}

        result = self.service.set_fields("TEST","TEST","TEST")

        self.assertEqual(result, {'status':True,'msj':'Success'})