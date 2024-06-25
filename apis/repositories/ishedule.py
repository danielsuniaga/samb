
from abc import ABC, abstractmethod

class irepositories_shedule(ABC):

    @abstractmethod
    def get(self,hour):
        pass

