import apis.services.dates.dates as case_dates

class controller_now_manager:

    dates = None

    def __init__(self):

        self.dates = case_dates.cases_dates()

    def get_now_manager(self):

        return self.dates.get_current_utc5()