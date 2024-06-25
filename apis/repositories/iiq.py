
from abc import ABC, abstractmethod

class irepositories_iq(ABC):

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
    def set_complement_start_date(self,date):
        pass

    @abstractmethod
    def seteo_count(self):
        pass

    @abstractmethod
    def get_current_entrys(self,date):
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

    @abstractmethod
    def get_sum_entrys_date(self,date):
        pass

    @abstractmethod
    def get_type_manager_day(self,day):
        pass
