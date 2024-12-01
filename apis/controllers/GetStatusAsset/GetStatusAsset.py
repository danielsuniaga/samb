from django.db import connection

from decouple import config

import apis.services.iq.iq as case_iq

import apis.services.config.config as case_config

import apis.services.telegram.telegram as case_telegram

import apis.services.dates.dates as case_dates

class controller_get_status_asset:
    
    iq = None

    config = None

    telegram = None

    dates = None

    project_name = None

    def __init__(self):

        cursor = connection.cursor()

        self.dates = case_dates.cases_dates()

        self.config = case_config.cases_config(cursor)

        self.iq = case_iq.cases_iq(cursor)

        self.iq.init_config(self.config)

        self.telegram = case_telegram.cases_telegram(cursor)

        self.project_name = config("PROJECT_NAME")

    def iq_init(self):

        return self.iq.init()
    
    def get_project_name(self):

        return self.project_name
    
    def iq_set_balance(self):

        return self.iq.set_balance()
    
    def iq_check(self):

        return self.iq.check()
    
    def iq_check_active_access(self):

        return self.iq.check_active_access()
    
    def iq_set_asset_financial(self):

        return self.iq.set_asset_financial()

    def telegram_send(self,msj):

        mensaje = self.get_project_name()+" = "+msj

        return self.telegram.send_without_persistence(mensaje)
    
    def init_operaciones(self):

        return [

            self.iq_init,

            lambda: self.iq.set_balance(self.dates),
            
            self.iq_check
        ]

    def get_status_asset(self):

        operaciones = self.init_operaciones()

        for operacion in operaciones:

            result = operacion()

            if not result['status']:
                
                return self.telegram_send(result['message'])
        
        return self.telegram_send(self.iq_check_active_access())