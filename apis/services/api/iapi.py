
from abc import ABC, abstractmethod

class icases_api(ABC):

    @abstractmethod
    def get_api_result(self):
        pass

    @abstractmethod
    def get_api_key(self, request):
        pass
