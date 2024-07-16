from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.shedule.shedule import cases_shedule

class TestServicesShedule(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_shedule(self.mock_cursor)

    @mock.patch('apis.repositories.shedule.repositories_shedule.get')
    def test_get_shedule_result(self, mock_get):

        mock_get.return_value = {'status':True,'msj':'Success'}

        result = self.service.get_shedule_result(8)

        self.assertEqual(result, {'status':True,'msj':'Success'})