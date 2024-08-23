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

import uuid
import time
import pytz
import os
import requests

class TestConnectionTelegram(APIView):

    base_url = 'https://api.telegram.org/bot6392837248:AAFDlXxJeTalDKIglpX4B5pVj3SClG9rjRc/sendMessage'

    def enviar_mensaje(self,chat_id, mensaje):

        url = self.base_url + 'sendMessage'
        
        params = {
        
            'chat_id': chat_id,
        
            'text': mensaje
        
        }
        
        response = requests.post(url, params=params)
        
        if response.status_code == 200:

            return True, "True"
        
        else:

            return False,"Error al enviar el mensaje. Código de respuesta:", response.status_code
        

    """ API para tester la conexxion con Telegram"""

    def get(self, request, format=None):

        return Response({self.enviar_mensaje('5226081927', '¡Hola desde Python jugada!')})

class GetDayWeek(APIView):

     def __init__(self):

          self.dates = case_dates.cases_dates()

     def post(self, request, format=None):

          return Response(self.dates.get_day())

class TestEndPoint(APIView):

     def __init__(self):

          cursor = connection.cursor()

          self.framework = case_framework.cases_framework(cursor)

          self.dates = case_dates.cases_dates()

     def post(self, request, format=None):

          now = self.dates.get_current_utc5()

          api_key="Test"

          return Response(self.framework.add(self.framework.generate_id(),self.dates.get_current_date(now),api_key))
     
class NowManager(APIView):

     def __init__(self):

          self.dates = case_dates.cases_dates()

     def post(self, request, format=None):

          now = self.dates.get_current_utc5()

          return Response(now)
     
class TestIq(APIView):

     def get(self, request, format=None):
          
          return Response({'status':True,'message':"Test"})
     
class TestMailSmtp(APIView):

     def __init__(self):

          cursor = connection.cursor()

          self.dates = case_dates.cases_dates()

          self.smtp = case_smtps.cases_smtp(cursor)

     def get(self, request, format=None):

          now = self.dates.get_current_utc5()

          self.dates.set_start_date()

          date = self.dates.get_current_date(now)

          return Response(self.smtp.send_notification_email(date, 'TEST ENVIO'))               

class GetReports(APIView):

     def __init__(self):

          cursor = connection.cursor()

          self.dates = case_dates.cases_dates()

          self.smtp = case_smtps.cases_smtp(cursor)

     def post(self, request, format=None):

          now = self.dates.get_current_utc5()

          self.dates.set_start_date()

          date = self.dates.get_current_date(now)

          self.smtp.set_end_date_repository(self.smtp.get_end_date())

          self.smtp.set_start_date_repository(self.smtp.get_start_date())

          self.smtp.set_subject_reports(self.smtp.get_subject_reports_nominal())

          self.smtp.send_reporting_email(date)

          self.smtp.set_end_date_repository(self.smtp.get_end_date_another())

          self.smtp.set_start_date_repository(self.smtp.get_start_date_another())   

          self.smtp.set_subject_reports(self.smtp.get_subject_reports_another())

          self.smtp.send_reporting_email(date)  

          return Response(True)
class GetDataAnalysisIqOptionClean(APIView):

     def __init__(self):

          cursor = connection.cursor()

          self.cronjobs = case_cronjobs.cases_cronjobs(cursor)

          self.dates = case_dates.cases_dates()

          self.shedules = case_shedules.cases_shedule(cursor)

          self.smtp = case_smtps.cases_smtp(cursor)

          self.api = case_apis.cases_api(cursor)

          self.iq = case_iq.cases_iq(cursor)

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
          
          result = self.iq.get_loops(self.dates,self.smtp,id_cronjobs,self.telegram)

          now = self.dates.get_current_utc5()

          self.dates.set_end_date()
          
          return Response(self.cronjobs.set_fields(self.dates.get_current_date(now),self.dates.get_time_execution(),id_cronjobs))
               
class GetDataAnalysisIqOption(APIView):
     
     """API que va a extraer y procesar la data escrita por la interacción de IqOption"""

     def post(self, request, format=None):

          return True

class AddModelRegressionLogistic(APIView):

     def __init__(self):

          cursor = connection.cursor()

          self.logistic_regression = case_logistic_regression.case_logistic_regression(cursor)

     def post(self, request, format=None):

          if not self.logistic_regression.add_dataset_historic():

               return Response(False)

          return Response(self.logistic_regression.generate_training())