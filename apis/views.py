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

# Your own imports
import apis.cases as cases

import uuid
import time
import pytz
import os

class TestEndPoint(APIView):

     def get(self, request, format=None):

          SECRET_KEY = config("SECRET_KEY")

          return Response({'status':False,'message':SECRET_KEY})
     
class TestEndSecrets(APIView):

     def get(self, request, format=None):
          
          return Response({'status':True,'message':"Test"})
     
class GetDataAnalysisIqOption(APIView):
     
     """API que va a extraer y procesar la data escrita por la interacción de IqOption"""

     def post(self, request, format=None):

          with connection.cursor() as cursor:

               _object_cases = cases.class_cases(cursor)

               _id_cronjobs = _object_cases.generate_cronjob_id()
               
               _now = _object_cases.get_current_utc5()

               _hour = _object_cases.get_current_hour(_now)

               _result = _object_cases.get_shedule_result(_hour)

               if not _result['status']:

                    return _object_cases.send_notification_email(_now, _result['msj'])

               _result = _object_cases.get_api_result()

               if not _result['status']:

                    return _object_cases.send_notification_email(_now, _result['msj'])
               
               _result = _object_cases.write_cronjobs(_id_cronjobs,_now)

               if not _result['status']:

                    return _object_cases.send_notification_email(_now, _result['msj'])

               return Response(False)
          
