from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.iq import cases_iq

class TestServicesTelegram(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_iq(self.mock_cursor)