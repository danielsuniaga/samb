from unittest import TestCase, mock

from apis.repositories.cronjobs import repositories_cronjobs

class TestRepositoriesCronjobs(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_cronjobs(self.mock_cursor)

    def test_set_id_financial_asset(self):

        new_value = "789"

        result = self.repo.set_id_financial_asset(new_value)
        
        self.assertEqual(self.repo.id_financial_asset, new_value)

        self.assertTrue(result)

    def test_get_success(self):

        result = self.repo.get()

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_add_success(self):

        result = self.repo.add('TEST', '2023-05-30')

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_set_fields_success(self):

        end_date = "2024-06-01"

        execute_time = "12:00:00"

        id_cronjobs = 1

        self.mock_cursor.execute.return_value = None

        result = self.repo.set_fields(end_date, execute_time, id_cronjobs)
        
        self.assertEqual(result, {'status': True, 'msj': 'Success'})

