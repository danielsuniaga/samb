from django.db import connection

import apis.services.cronjobs.cronjobs as case_cronjobs

import apis.services.dates.dates as case_dates

import apis.services.shedule.shedule as case_shedules

import apis.services.smtp.smtp as case_smtps

import apis.services.api.api as case_apis

import apis.services.iq.iq as case_iq

import apis.services.telegram.telegram as case_telegram

import apis.services.machine_learning.logistic_regression as case_logistic_regression

import apis.services.config.config as case_config

import apis.services.events.events as case_events

class controller_get_data_analysis_iq_option_clean:

    cursor = None

    cronjobs = None

    dates = None

    shedules = None

    smtp = None

    api = None

    iq = None

    telegram = None

    logistic_regression = None

    event = None

    config = None

    def __init__(self):

        cursor = connection.cursor()

        self.cronjobs = case_cronjobs.cases_cronjobs(cursor)

        self.dates = case_dates.cases_dates()

        self.shedules = case_shedules.cases_shedule(cursor)

        self.smtp = case_smtps.cases_smtp(cursor)

        self.api = case_apis.cases_api(cursor)

        self.iq = case_iq.cases_iq(cursor)

        self.telegram = case_telegram.cases_telegram(cursor)

        self.logistic_regression = case_logistic_regression.case_logistic_regression(cursor)

        self.logistic_regression.init_object_date(self.dates)

        self.events = case_events.cases_events()

        self.config = case_config.cases_config(cursor)

        self.iq.init_config(self.config)

    def get_data_analysis_iq_option_clean(self,request):

        self.events.set_events_field('start_endpoint',self.dates.get_current_date_mil_dynamic())

        id_cronjobs = self.cronjobs.generate_cronjob_id()

        now = self.dates.get_current_utc5()

        self.dates.set_start_date()

        date = self.dates.get_current_date(now)

        hour = self.dates.get_current_hour(now)

        result = self.api.get_api_key(request)

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        result = self.shedules.get_shedule_result(hour)

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        result = self.api.get_api_result()

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        result = self.cronjobs.add(id_cronjobs,date)

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        self.events.set_events_field('init_endpoint',self.dates.get_current_date_mil_dynamic())

        result = self.iq.init()

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        self.events.set_events_field('init_broker',self.dates.get_current_date_mil_dynamic())
          
        result = self.iq.set_balance(self.dates)

        if not result['status']:

            return self.smtp.send_notification_email(date, result['msj'])
        
        self.events.set_events_field('config_broker',self.dates.get_current_date_mil_dynamic())
          
        self.iq.init_regression_logistic_model_general(self.logistic_regression)

        self.iq.init_events(self.events)
        
        return self.iq.get_loops(self.dates,self.smtp,id_cronjobs,self.telegram)

        now = self.dates.get_current_utc5()

        self.dates.set_end_date()

        return self.cronjobs.set_fields(self.dates.get_current_date(now),self.dates.get_time_execution(),id_cronjobs)