
from abc import ABC, abstractmethod

class irepositories_cronjobs(ABC):

    @abstractmethod
    def set_id_financial_asset(self,value):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self,id_cronjobs,fecha_actual):
        pass

    @abstractmethod
    def set_fields(self,end_date,execute_time,id_cronjobs):
        pass
