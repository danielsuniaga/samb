from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status, filters

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated# Create your views here.

from django.db import connection

import apis.src.class_api as api

import apis.src.class_cronjobs as cronjobs

import apis.src.class_notifications as notifications

import apis.src.class_date as custom_date

import uuid

import time

import pytz

import os

class TestEndPoint(APIView):

     def get(self, request, format=None):

          secret = os.environ.get('EMAIL_PASSWORD')

          # print(f"Valor de SECRET_PASSWORD: {secret}")
          
          return Response({'status':True,'message':secret})
     
class TestEndSecrets(APIView):

     def get(self, request, format=None):

          # email_password = os.environ.get('EMAIL_PASSWORD')
          
          return Response({'status':True,'message':"Test"})
     
class GetDataAnalysisIqOption(APIView):
     
     """API que va a extraer y procesar la data escrita por la interacción de IqOption"""

     cursor = connection.cursor()

     api_description='get-data-analysis-iqoption'

     par='EURUSD'

     def post(self, request, format=None):

          _id_cronjobs =  uuid.uuid4().hex

          _object_date = custom_date.class_date()

          _now = _object_date.get_utc5()

          _object_api = api.class_apis(self.api_description,self.cursor)

          _object_smtp = notifications.class_smtp(_now,self.cursor)

          _result = _object_api.get()

          if not _result['status']:

               return Response(_object_smtp.send(_result['msj']))

               # return Response(_result)
          
          
          _object_cronjobs = cronjobs.class_cronjobs(self.api_description,self.cursor,self.par,_id_cronjobs,_now,'2')
     
          return Response(_object_cronjobs.write())
          
