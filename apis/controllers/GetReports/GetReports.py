from django.db import connection

import apis.services.dates.dates as case_dates

import apis.services.smtp.smtp as case_smtps

class controller_get_reports:

    cursor = None
    
    dates = None

    smtp = None

    def __init__(self):

        self.cursor = connection.cursor()

        self.dates = case_dates.cases_dates()

        self.smtp = case_smtps.cases_smtp(self.cursor)

    def get_reports(self):

        now = self.dates.get_current_utc5()

        self.dates.set_start_date()

        date = self.dates.get_current_date(now)

        self.smtp.set_end_date_repository(self.smtp.get_end_date())

        self.smtp.set_start_date_repository(self.smtp.get_start_date())

        self.smtp.set_subject_reports(self.smtp.get_subject_reports_nominal())

        self.smtp.send_reporting_email(date)

        return True