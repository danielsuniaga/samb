
from abc import ABC, abstractmethod

class icases_cronjobs(ABC):

    @abstractmethod
    def generate_cronjob_id(self):
        pass

    @abstractmethod
    def add(self,id_cron,fecha):
        pass

    @abstractmethod
    def set_fields(self,end_date,execute_time,id_cronjobs):
        pass
