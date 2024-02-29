from datetime import datetime
from decouple import config
from datetime import timedelta

import time

import pytz

class cases_dates:

    def __init__(self):

        self.second=int(config("SLEEP"))

        self.start_date = None

        self.end_date = None

    def set_start_date(self):

        self.start_date = time.time()

    def set_end_date(self):

        self.end_date = time.time()

    def get_time_execution(self):

        return self.end_date-self.start_date

    def get_current_utc5(self):

        # Obtén la fecha y hora actual en UTC
        now_utc = datetime.utcnow()

        # Define la zona horaria deseada (UTC-5)
        tz = pytz.timezone('America/New_York')  # Puedes cambiar 'America/New_York' por la zona horaria deseada

        # Ajusta la fecha y hora a la zona horaria deseada
        return now_utc.replace(tzinfo=pytz.utc).astimezone(tz)
    
    def get_current_date(self,date):

        return date.strftime("%Y%m%d%H%M%S")
    
    def get_current_hour(self,hour):

        return hour.strftime("%H%M%S")
    
    def get_current_date_only(self,date):

        return date.strftime("%Y%m%d")
    
    def get_current_date_minus_minutes(self,date,minutos):

        return date - timedelta(minutes=minutos)
    
    def get_seconds_next_minute(self):

        now = self.get_current_utc5()

        return self.second - now.second
    
    def get_day(self):

        now = self.get_current_utc5()

        # basico

        return now.weekday()
