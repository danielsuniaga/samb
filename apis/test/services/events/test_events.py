from unittest import TestCase, mock

from unittest.mock import patch

import unittest

import apis.services.events.events as case_events

class TestServicesEvents(TestCase):

    service = None

    def setUp(self):

        self.service = case_events.cases_events()

    def test_generate_msj_events(self):

        self.service.init_events()

        result = self.service.generate_msj_events()

        print(result)