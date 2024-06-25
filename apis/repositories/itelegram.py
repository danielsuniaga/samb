
from abc import ABC, abstractmethod

class irepositories_telegram(ABC):

    @abstractmethod
    def send(self, mensaje):
        pass

    @abstractmethod
    def add(self,mensaje,response,id_cronjobs,fecha):
        pass
