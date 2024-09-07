from datetime import datetime
from decouple import config
from datetime import timedelta
from apis.services.dates.idates import icases_dates

import time

import pytz

class cases_dates(icases_dates):

    def __init__(self):

        self.second=int(config("SLEEP"))

        self.start_date = None

        self.end_date = None

    def set_start_date(self):

        self.start_date = time.time()

        return True

    def set_end_date(self):

        self.end_date = time.time()

        return True

    def get_time_execution(self):

        return self.end_date-self.start_date

    def get_current_utc5(self):

        # Obtén la fecha y hora actual en UTC con información de zona horaria
        now_utc = datetime.now(pytz.utc)

        # Define la zona horaria deseada (UTC-5)
        tz = pytz.timezone('America/Bogota')  # Puedes cambiar 'America/New_York' por la zona horaria deseada
        
        # Ajusta la fecha y hora a la zona horaria deseada
        return now_utc.astimezone(tz)
    
    def get_current_date(self,date):

        return date.strftime("%Y%m%d%H%M%S")
    
    def get_current_date_specific(self,date,specific):

        return date.strftime(specific)
    
    def generate_date_to_str(self,str):

        return datetime.strptime(str, "%Y%m%d%H%M%S%f")
    
    def get_current_date_mil(self,date):

        return date.strftime("%Y%m%d%H%M%S%f")[:-3]
    
    def get_current_date_mil_front(self,date):

        return date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
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

        return now.weekday()
    
    def get_current_date_mil_dynamic(self):

        now = self.get_current_utc5()

        return self.get_current_date_mil(now)
