import apis.repositories.notification as repository_notifications

from decouple import config

import json

import requests

from apis.services.telegram.itelegram import icases_telegram

class cases_telegram(icases_telegram):

    def __init__(self,cursor):

        self.telegram = repository_notifications.repositories_telegram(cursor)

    def translate_dictionary_json(self,value):

        return json.dumps(value)

    def send(self, mensaje,id_cronjobs,date):

        return self.telegram.add(mensaje,self.translate_dictionary_json(self.telegram.send(mensaje)),id_cronjobs,date)

