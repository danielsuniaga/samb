from unittest import TestCase, mock

from apis.repositories.shedule import repositories_shedule

class TestRepositoriesShedule(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_shedule(self.mock_cursor)

    def test_get_success(self):

        self.mock_cursor.execute.return_value = 1

        hour=23

        result = self.repo.get(hour)

        self.assertEqual(result, {'status': True, 'msj': 'Success'})