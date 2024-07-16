from unittest import TestCase, mock

from apis.repositories.framework.framework import repositories_framework

class TestRepositoriesFramework(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_framework(self.mock_cursor)

    def test_add_success(self):

        result = self.repo.add(1, '2023-05-30', 'Test description')

        self.assertEqual(result, {'status': True, 'msj': 'Success'})

    def test_get(self):

        result = self.repo.get()

        self.assertEqual(result, {'status': True, 'msj': 'Success'})