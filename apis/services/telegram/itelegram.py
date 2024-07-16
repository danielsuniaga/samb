
from abc import ABC, abstractmethod

class icases_telegram(ABC):

    @abstractmethod
    def translate_dictionary_json(self,value):
        pass

    @abstractmethod
    def send(self, mensaje,id_cronjobs,date):
        pass