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
import apis.services.cronjobs as case_cronjobs
import apis.services.dates as case_dates
import apis.services.shedule as case_shedules
import apis.services.smtp as case_smtps
import apis.services.api as case_apis
import apis.services.iq as case_iq
import apis.services.framework as case_framework
import apis.services.telegram as case_telegram

import uuid
import time
import pytz
import os
import requests

class TestConnectionTelegram(APIView):

    base_url = 'https://api.telegram.org/bot6392837248:AAFDlXxJeTalDKIglpX4B5pVj3SClG9rjRc/sendMessage'

    # CHAT_ID = '5226081927'

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

        # _msj="test v1"

        # self.enviar_mensaje("¡Hola desde Python!")

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

          api_key = request.headers.get('X-API-Key')

          return Response(self.framework.add(self.framework.generate_id(),self.dates.get_current_date(now),api_key))
     
class TestIq(APIView):

     def get(self, request, format=None):
          
          return Response({'status':True,'message':"Test"})
     
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
          
          result = self.iq.set_balance()

          if not result['status']:

               return Response(self.smtp.send_notification_email(date, result['msj']))
          
          result = self.iq.get_loops(self.dates,self.smtp,id_cronjobs,self.telegram)

          now = self.dates.get_current_utc5()

          self.dates.set_end_date()

          result = self.cronjobs.set_fields(self.dates.get_current_date(now),self.dates.get_time_execution(),id_cronjobs)
          
          return Response(result)
               
class GetDataAnalysisIqOption(APIView):
     
     """API que va a extraer y procesar la data escrita por la interacción de IqOption"""

     def post(self, request, format=None):

          return True

          # with connection.cursor() as cursor:

          #      _object_cases = cases.class_cases(cursor)

          #      _id_cronjobs = _object_cases.generate_cronjob_id()
               
          #      _now = _object_cases.get_current_utc5()

          #      _date = _object_cases.get_current_date(_now)

          #      _hour = _object_cases.get_current_hour(_now)

          #      _result = _object_cases.get_shedule_result(_hour)

          #      if not _result['status']:

          #           return _object_cases.send_notification_email(_date, _result['msj'])

          #      _result = _object_cases.get_api_result()

          #      if not _result['status']:

          #           return _object_cases.send_notification_email(_date, _result['msj'])
               
          #      _result = _object_cases.write_cronjobs(_id_cronjobs,_date)

          #      if not _result['status']:

          #           return _object_cases.send_notification_email(_date, _result['msj'])
               
          #      _result = _object_cases.init_iq()

          #      if not _result['status']:

          #           return _object_cases.send_notification_email(_date, _result['msj'])
               
          #      _result = _object_cases.set_balance()

          #      if not _result['status']:

          #           return _object_cases.send_notification_email(_date, _result['msj'])

          #      return Response(_object_cases.entrys())
          
