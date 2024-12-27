from unittest import TestCase, mock

import apis.controllers.GetDataAnalysisDerivClean.GetDataAnalysisDerivClean as controller_get_data_analysis_deriv_clean

from django.db import connection

class TestGetDataAnalysisDerivClean(TestCase):

    cursor = None

    controller = None

    def setUp(self):

        self.controller = controller_get_data_analysis_deriv_clean.controller_get_data_analysis_deriv_clean()

    def test_get_data_analysis_deriv_clean(self):

        result = self.controller.get_data_analysis_deriv_clean()

        print(result)

        