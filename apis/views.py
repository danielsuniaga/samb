# Django imports
from django.shortcuts import render
from django.db import connection

# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# Third-party imports
from decouple import config
from iqoptionapi.stable_api import IQ_Option

# Your own imports
# import apis.cases as cases
import apis.services.cronjobs.cronjobs as case_cronjobs
import apis.services.dates.dates as case_dates
import apis.services.shedule.shedule as case_shedules
import apis.services.shedule.shedule_another as cases_shedule_another
import apis.services.smtp.smtp as case_smtps
import apis.services.api.api as case_apis
import apis.services.iq.iq as case_iq
import apis.services.iq.iq_another as case_iq_another
import apis.services.framework.framework as case_framework
import apis.services.telegram.telegram as case_telegram
import apis.services.machine_learning.logistic_regression as case_logistic_regression
import apis.services.events.events as case_events
import apis.services.metrics_evaluation_model.metrics_evaluation_model as case_metrics_evaluation_model

import apis.controllers.TestEndPoint.TestEndPoint as controller_test_end_point
import apis.controllers.NowManager.NowManager as controller_now_manager
import apis.controllers.GetReports.GetReports as controller_get_reports
import apis.controllers.GetDataAnalysisIqOptionClean.GetDataAnalysisIqOptionClean as controller_get_data_analysis_iq_option_clean


import uuid
import time
import pytz
import os
import requests

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

     def __init__(self):

          cursor = connection.cursor()

          self.cronjobs = case_cronjobs.cases_cronjobs(cursor)

          self.dates = case_dates.cases_dates()

          self.shedules = cases_shedule_another.cases_shedule_another(cursor)

          self.smtp = case_smtps.cases_smtp(cursor)

          self.api = case_apis.cases_api(cursor)

          self.iq = case_iq_another.cases_iq_another(cursor)

          self.telegram = case_telegram.cases_telegram(cursor)

          self.logistic_regression = case_logistic_regression.case_logistic_regression(cursor)

          self.logistic_regression.init_object_date(self.dates)

     def post(self, request, format=None):
          
          id_cronjobs = self.cronjobs.generate_cronjob_id()

          now = self.dates.get_current_utc5()

          self.dates.set_start_date()

          date = self.dates.get_current_date(now)

          hour = self.dates.get_current_hour(now)

          result = self.api.get_api_key(request)

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.shedules.get_shedule_result(hour)

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.api.get_api_result()

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.cronjobs.add(id_cronjobs,date)

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.iq.init()

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.iq.set_balance(self.dates)

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          self.iq.init_regression_logistic_model_general(self.logistic_regression)
          
          self.iq.get_loops(self.dates,self.smtp,id_cronjobs,self.telegram)

          now = self.dates.get_current_utc5()

          self.dates.set_end_date()
          
          return Response(self.cronjobs.set_fields(self.dates.get_current_date(now),self.dates.get_time_execution(),id_cronjobs))
               
class GetDataAnalysisIqOption(APIView):
     
     """API que va a extraer y procesar la data escrita por la interacción de IqOption"""

     def post(self, request, format=None):

          return True

class AddModelRegressionLogistic(APIView):

     cursor = None

     date = None

     telegram  = None

     logistic_regression = None

     metrics_evaluation_model = None

     def __init__(self):

          cursor = connection.cursor()

          self.dates = case_dates.cases_dates()

          self.telegram = case_telegram.cases_telegram(cursor)

          self.logistic_regression = case_logistic_regression.case_logistic_regression(cursor)

          self.metrics_evaluation_model = case_metrics_evaluation_model.case_metrics_evaluation_model(cursor)

          self.logistic_regression.init_object_date(self.dates)
          
          self.logistic_regression.init_object_telegram(self.telegram)

          self.logistic_regression.init_object_object_metrics_evaluation_model(self.metrics_evaluation_model)

     def post(self, request, format=None):

          if not self.logistic_regression.add_dataset_historic():

               return Response(False)
                    
          return Response(self.logistic_regression.generate_training())