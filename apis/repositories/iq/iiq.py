
from abc import ABC, abstractmethod

class irepositories_iq(ABC):

    @abstractmethod
    def set_complement_start_date(self,valor):
        pass

    @abstractmethod
    def set_complement_end_date(self,date):
        pass

    @abstractmethod
    def get_current_entrys(self,date):
        pass

    @abstractmethod
    def get_sum_entrys_date(self,date):
        pass

    @abstractmethod
    def get_type_manager_day(self,day):
        pass