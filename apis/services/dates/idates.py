
from abc import ABC, abstractmethod

class icases_dates(ABC): 

    @abstractmethod
    def set_start_date(self):
        pass
    
    @abstractmethod
    def set_end_date(self):
        pass
    
    @abstractmethod
    def get_time_execution(self):
        pass
    
    @abstractmethod
    def get_current_utc5(self):
        pass
    
    @abstractmethod
    def get_current_date(self, date):
        pass
    
    @abstractmethod
    def get_current_hour(self, hour):
        pass
    
    @abstractmethod
    def get_current_date_only(self, date):
        pass
    
    @abstractmethod
    def get_current_date_minus_minutes(self, date, minutos):
        pass
    
    @abstractmethod
    def get_seconds_next_minute(self):
        pass
    
    @abstractmethod
    def get_day(self):
        pass