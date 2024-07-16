
from abc import ABC, abstractmethod

class irepositories_smtp(ABC):

    @abstractmethod
    def set_message_report(self,valor):
        pass

    @abstractmethod
    def get_structura_reporte(self,mensaje):
        pass

    @abstractmethod
    def get_encabezado(self):
        pass

    @abstractmethod
    def get_pie(self):
        pass

    @abstractmethod
    def set_message(self,mensaje):
        pass

    @abstractmethod
    def set_message_body(self):
        pass

    @abstractmethod
    def send(self,fecha,mensaje):
        pass

    @abstractmethod
    def send_reports(self,fecha,mensaje):
        pass

    @abstractmethod
    def get_data_reporting(self,mode,day):
        pass

    @abstractmethod
    def get_data_reporting_cur(self,mode):
        pass

    @abstractmethod
    def get_data_reporting_tot(self, mode):
        pass

