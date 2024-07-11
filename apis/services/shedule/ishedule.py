
from abc import ABC, abstractmethod

class icases_shedule(ABC):

    @abstractmethod
    def get_shedule_result(self,hour):
        pass