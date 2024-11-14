from django.db import connection

import apis.services.dates.dates as case_dates

import apis.services.framework.framework as case_framework

class controller_test_end_point:

    framework = None

    dates = None

    def __init__(self):

        cursor = connection.cursor()

        self.framework = case_framework.cases_framework(cursor)

        self.dates = case_dates.cases_dates()

    def add_framework(self):

        now = self.dates.get_current_utc5()

        api_key="Test"

        return self.framework.add(self.framework.generate_id(),self.dates.get_current_date(now),api_key)