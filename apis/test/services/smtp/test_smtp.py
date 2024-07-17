from unittest import TestCase, mock

from unittest.mock import patch,Mock

from apis.services.smtp.smtp import cases_smtp

class TestServicesSmtp(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_smtp(self.mock_cursor)

    @mock.patch('apis.repositories.notification.notification.repositories_smtp.send')
    def test_send_notification_email(self, mock_get):

        mock_get.return_value = True

        result = self.service.send_notification_email("20240606","TEST")

        self.assertTrue(result)

    @mock.patch('apis.repositories.notification.notification.repositories_smtp.send_reports')
    def test_send_reporting_email(self, mock_get):

        mock_get.return_value = True

        result = self.service.send_reporting_email("20240606")

        self.assertTrue(result)

    def test_init_data_days(self):

        expected_result = [
            {"name":"Actually","database":0},
            {"name":"Monday","database":2},
            {"name":"Tuesday","database":3},
            {"name":"Wednesday","database":4},
            {"name":"Thursday","database":5},
            {"name":"Friday","database":6},
            {"name":"Saturday","database":7},
            {"name":"Sunday","database":1},
            {"name":"Total","database":9}
        ]

        result = self.service.init_data_days()

        self.assertEqual(result, expected_result)

    @mock.patch('apis.repositories.notification.notification.repositories_smtp.get_data_reporting_cur')
    def test_get_data_repository_cur(self, mock_get):

        mock_get.return_value = "Cur_data"

        result = self.service.get_data_repository("PRACTICE", 0)

        self.assertEqual(result, "Cur_data")

    @mock.patch('apis.repositories.notification.notification.repositories_smtp.get_data_reporting')
    def test_get_data_repository(self, mock_get):

        mock_get.return_value = "Other_data"

        result = self.service.get_data_repository("PRACTICE", 3)

        self.assertEqual(result, "Other_data")

    @mock.patch('apis.repositories.notification.notification.repositories_smtp.get_data_reporting_tot')
    def test_get_data_repository_tot(self, mock_get):

        mock_get.return_value = "Tot_data"

        result = self.service.get_data_repository("PRACTICE", 9)

        self.assertEqual(result, "Tot_data")

    def test_structure_registry_data(self):

        data = {"name": "Monday", "database": 2}

        self.service.get_data_repository = Mock(side_effect=lambda mode, database: f"{mode}_data_{database}")

        expected_result = {"day": "Monday", "demo": "PRACTICE_data_2", "real": "REAL_data_2"}

        result = self.service.structure_registry_data(data)

        self.assertEqual(result, expected_result)

    def test_init_data_reporting(self):

        self.service.init_data_days = Mock(return_value=[
            {"name": "Actually", "database": 0},
            {"name": "Monday", "database": 2},
            {"name": "Tuesday", "database": 3}
        ])

        self.service.structure_registry_data = Mock(side_effect=[
            {"day": "Actually", "demo": "PRACTICE_data_0", "real": "REAL_data_0"},
            {"day": "Monday", "demo": "PRACTICE_data_2", "real": "REAL_data_2"},
            {"day": "Tuesday", "demo": "PRACTICE_data_3", "real": "REAL_data_3"}
        ])

        expected_result = [
            {"day": "Actually", "demo": "PRACTICE_data_0", "real": "REAL_data_0"},
            {"day": "Monday", "demo": "PRACTICE_data_2", "real": "REAL_data_2"},
            {"day": "Tuesday", "demo": "PRACTICE_data_3", "real": "REAL_data_3"}
        ]

        result = self.service.init_data_reporting()

        self.assertEqual(len(result), 3)

        self.assertEqual(result, expected_result)

    def test_get_format_data_reporting(self):

        registro = {"day": "Monday", "demo": "PRACTICE_data_2", "real": "REAL_data_2"}

        expected_result = """ <tr><td>Monday</td><td>PRACTICE_data_2</td><td>REAL_data_2</td></tr> """

        result = self.service.get_format_data_reporting(registro)

        self.assertEqual(result, expected_result)

    def test_get_data_reporting(self):

        data = [
            {"day": "Monday", "demo": "PRACTICE_data_2", "real": "REAL_data_2"},
            {"day": "Tuesday", "demo": "PRACTICE_data_3", "real": "REAL_data_3"}
        ]

        expected_result = """ <tr><td>Monday</td><td>PRACTICE_data_2</td><td>REAL_data_2</td></tr> """ + \
                          """ <tr><td>Tuesday</td><td>PRACTICE_data_3</td><td>REAL_data_3</td></tr> """

        result = self.service.get_data_reporting(data)

        self.assertEqual(result, expected_result)
    
    def test_data_reporting(self):

        self.service.get_data_reporting = Mock(return_value="PRACTICE_data_0")

        expected_result = "PRACTICE_data_0"

        result = self.service.data_reporting()

        self.assertEqual(result, expected_result)