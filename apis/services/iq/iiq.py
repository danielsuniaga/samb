
from abc import ABC, abstractmethod

class icases_iq(ABC): 

    @abstractmethod
    def analized_candles(self,valor):
        pass
    
    @abstractmethod
    def analized_mode(self,valor):
        pass
    
    @abstractmethod
    def set_balance(self,valor):
        pass
    
    @abstractmethod
    def analized_day(self,valor):
        pass
    
    @abstractmethod
    def set_asset_financial(self, valor):
        pass
    
    @abstractmethod
    def get_loops(self):
        pass