
from abc import ABC, abstractmethod

class irepositories_framework(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self,id_framework,fecha,description):
        pass