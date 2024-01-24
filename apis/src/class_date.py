from datetime import datetime

from datetime import timedelta

import time

import pytz

class class_date:

    current_date = ""

    def get_utc5(self):

        # Obtén la fecha y hora actual en UTC
        now_utc = datetime.utcnow()

        # Define la zona horaria deseada (UTC-5)
        tz = pytz.timezone('America/New_York')  # Puedes cambiar 'America/New_York' por la zona horaria deseada

        # Ajusta la fecha y hora a la zona horaria deseada
        return now_utc.replace(tzinfo=pytz.utc).astimezone(tz)

