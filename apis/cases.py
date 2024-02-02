from rest_framework.response import Response

import apis.src.class_date as custom_date
import apis.src.class_shedule as shedule
import apis.src.class_api as api
import apis.src.class_cronjobs as cronjobs
import apis.src.class_notifications as notifications

import uuid

# Third-party imports
from decouple import config

class class_cases:

    def __init__(self,cursor):

        self.api_description=config("API_DESCRIPTION")

        self.par=config("PAR")

        self.cursor_db = cursor

        self.object_date = custom_date.class_date()

        self.object_cronjobs = cronjobs.class_cronjobs()

    def generate_cronjob_id(self):

        return uuid.uuid4().hex
    
    def get_current_utc5(self):

        return self.object_date.get_utc5()
    
    def get_current_hour(self,hour):

        return hour.strftime("%H%M%S")
    
    def get_api_result(self):
        
        object_api = api.class_apis(self.api_description, self.cursor_db)

        return object_api.get()
    
    def get_shedule_result(self,hour):
        
        object_shedule = shedule.class_shedule(self.cursor_db)

        return object_shedule.get(hour)

    def send_notification_email(self, now, message):

        object_smtp = notifications.class_smtp(now, self.cursor_db)

        return Response(object_smtp.send(message))
    
    def write_cronjobs(self,id_cron,fecha):

        return self.object_cronjobs.write(id_cron,fecha,self.cursor_db)