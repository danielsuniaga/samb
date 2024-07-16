
from abc import ABC, abstractmethod

class irepositories_iq_core(ABC):

    @abstractmethod
    def set_mode(self,valor):
        pass

    @abstractmethod
    def get_mode(self):
        pass

    @abstractmethod
    def set_result_entry(self,valor):
        pass

    @abstractmethod
    def get_result_entry(self):
        pass

    @abstractmethod
    def get_id_entry(self):
        pass

    @abstractmethod
    def set_id_entry(self,valor):
        pass

    @abstractmethod
    def seteo_count(self):
        pass

    @abstractmethod
    def get_current_entrys_min(self,date,candles):
        pass

    @abstractmethod
    def add_entrys(self,current_date,id_cronjobs,type_operations,id_entry_platform):
        pass

    @abstractmethod
    def add_entrys_result(self,id_entry_result,current_date):
        pass

    @abstractmethod
    def add_indicators(self,id_tuple,current_date,id_indicators,value_indicators):
        pass