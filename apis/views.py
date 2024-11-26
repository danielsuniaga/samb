# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response

import apis.controllers.TestEndPoint.TestEndPoint as controller_test_end_point
import apis.controllers.NowManager.NowManager as controller_now_manager
import apis.controllers.GetReports.GetReports as controller_get_reports
import apis.controllers.GetDataAnalysisIqOptionClean.GetDataAnalysisIqOptionClean as controller_get_data_analysis_iq_option_clean
import apis.controllers.GetDataAnalysisIqOptionCleanAnother.GetDataAnalysisIqOptionCleanAnother as controller_get_data_analysis_iq_option_clean_another
import apis.controllers.AddModelRegressionLogistic.AddModelRegressionLogistic as controller_add_model_regression_logistic
import apis.controllers.GetStatusAsset.GetStatusAsset as controller_get_status_asset

class GetStatusAsset(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_get_status_asset.controller_get_status_asset()

     def post(self, request, format=None):

          return Response(self.controller.get_status_asset())

class TestEndPoint(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_test_end_point.controller_test_end_point()

     def post(self, request, format=None):

          return Response(self.controller.add_framework())
     
class NowManager(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_now_manager.controller_now_manager()

     def post(self, request, format=None):

          return Response(self.controller.get_now_manager())           

class GetReports(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_get_reports.controller_get_reports()

     def post(self, request, format=None):

          return Response(self.controller.get_reports())
class GetDataAnalysisIqOptionClean(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_get_data_analysis_iq_option_clean.controller_get_data_analysis_iq_option_clean()

     def post(self, request, format=None):

          return Response(self.controller.get_data_analysis_iq_option_clean(request))
     
class GetDataAnalysisIqOptionCleanAnother(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_get_data_analysis_iq_option_clean_another.controller_get_data_analysis_iq_option_clean_another()
          
     def post(self, request, format=None):

          return Response(self.controller.get_data_analysis_iq_option_clean(request))

class AddModelRegressionLogistic(APIView):

     controller = None

     def __init__(self):

          self.controller = controller_add_model_regression_logistic.controller_add_model_regression_logistic()

     def post(self, request, format=None):
                    
          return Response(self.controller.add_model_regression_logistic())