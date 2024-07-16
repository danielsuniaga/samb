
from abc import ABC, abstractmethod

class icases_framework(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self,id_framework,date,description):
        pass

    @abstractmethod
    def generate_id(self):
        pass

