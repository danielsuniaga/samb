from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.dates.dates import cases_dates

from datetime import timedelta,datetime

import pytz

class TestServicesDates(TestCase):

    def setUp(self):
        
        self.service = cases_dates()

        self.new_value = "TEST"

    def test_set_start_date(self):

        result = self.service.set_start_date()
        
        self.assertTrue(result)

    def test_set_end_date(self):

        result = self.service.set_end_date()
        
        self.assertTrue(result)

    def test_get_time_execution(self):

        self.service.start_date = datetime(2024, 1, 1, 10, 0, 0)

        self.service.end_date = datetime(2024, 1, 1, 12, 0, 0)

        execution_time = self.service.get_time_execution()

        expected_time = timedelta(hours=2)

        self.assertEqual(execution_time, expected_time)

    @patch('apis.services.dates.datetime')
    def test_get_current_utc5(self,mock_datetime):

        mock_datetime.now.return_value = datetime(2024, 6, 1, 12, 0, 0, tzinfo=pytz.utc)

        expected_time = datetime(2024, 6, 1, 7, 0, 0)

        expected_tz = pytz.timezone('America/Bogota')

        expected_time = expected_tz.localize(expected_time)

        current_time_utc5 = self.service.get_current_utc5()

        self.assertEqual(current_time_utc5, expected_time)

    def test_get_current_date(self):

        test_date = datetime(2024, 6, 1, 12, 0, 0)
        
        expected_result = "20240601120000"
        
        result = self.service.get_current_date(test_date)
        
        self.assertEqual(result, expected_result)

    def test_get_current_hour(self):

        test_date = datetime(2024, 6, 1, 12, 0, 0)
        
        expected_result = "120000"
        
        result = self.service.get_current_hour(test_date)
        
        self.assertEqual(result, expected_result)

    def test_get_current_date_only(self):

        test_date = datetime(2024, 6, 1, 12, 0, 0)
        
        expected_result = "20240601"
        
        result = self.service.get_current_date_only(test_date)
        
        self.assertEqual(result, expected_result)

    def test_get_current_date_minus_minutes(self):

        test_date = datetime(2024, 6, 1, 12, 0, 0)

        minutos = 30
        
        expected_result = test_date - timedelta(minutes=minutos)
        
        result = self.service.get_current_date_minus_minutes(test_date, minutos)
        
        self.assertEqual(result, expected_result)

    @patch('apis.services.dates.cases_dates.get_current_utc5')
    def test_get_seconds_next_minute(self, mock_get_current_utc5):

        timezone = pytz.timezone('America/Bogota')
        
        test_date = timezone.localize(datetime(2024, 6, 1, 12, 0, 45))
        
        mock_get_current_utc5.return_value = test_date

        expected_result = 60 - test_date.second
        
        result = self.service.get_seconds_next_minute()

        self.assertEqual(result, expected_result)

    @patch('apis.services.dates.cases_dates.get_current_utc5')
    def test_get_day(self, mock_get_current_utc5):

        timezone = pytz.timezone('America/Bogota')

        test_date = timezone.localize(datetime(2024, 6, 1, 12, 0, 0))
        
        mock_get_current_utc5.return_value = test_date

        expected_result = test_date.weekday()
        
        result = self.service.get_day()

        self.assertEqual(result, expected_result)