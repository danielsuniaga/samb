
from abc import ABC, abstractmethod

class irepositories_api(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_api_key(self,key,value):
        pass
