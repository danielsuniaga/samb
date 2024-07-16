
from abc import ABC, abstractmethod

class icases_smtp(ABC):

    @abstractmethod
    def send_notification_email(self,date,mensaje):
        pass

    @abstractmethod
    def send_reporting_email(self,date):
        pass

    @abstractmethod
    def get_data_repository(self,mode,day):
        pass

    @abstractmethod
    def structure_registry_data(self,data):
        pass

    @abstractmethod
    def init_data_days(self):
        pass

    @abstractmethod
    def init_data_reporting(self):
        pass

    @abstractmethod
    def init_data_reporting(self):
        pass

    @abstractmethod
    def get_format_data_reporting(self,registro):
        pass

    @abstractmethod
    def get_data_reporting(self,data):
        pass

    @abstractmethod
    def data_reporting(self):
        pass