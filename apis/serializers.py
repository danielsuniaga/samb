from rest_framework import serializers

from api import models

class GetIqOption(serializers.Serializer):

    """ Serieliza un campo para probar nuestra APIView integrando la API de Iq Option """

    par = serializers.CharField(max_length=10)