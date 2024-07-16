
from abc import ABC, abstractmethod

class irepositories_notifications(ABC):

    @abstractmethod
    def add_notificacion_exc(self,mensaje):
        pass

    @abstractmethod
    def add_reports(self):
        pass

    @abstractmethod
    def removed_special_characters(self,value):
        pass

    @abstractmethod
    def add_notification_telegram(self,mensaje,response,id_cronjobs):
        pass

    @abstractmethod
    def set_fecha(self,fecha):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_data_reporting_day(self,mode,day):
        pass

    @abstractmethod
    def get_data_reporting_curdate(self,mode):
        pass

    @abstractmethod
    def get_data_reporting_total(self,mode):
        pass
