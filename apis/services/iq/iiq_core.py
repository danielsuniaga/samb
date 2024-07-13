
from abc import ABC, abstractmethod

class icases_iq_core(ABC): 

    @abstractmethod
    def set_message(self,valor):
        pass
    
    @abstractmethod
    def add_message_text(self,valor):
        pass
    
    @abstractmethod
    def set_value_rsi(self,valor):
        pass
    
    @abstractmethod
    def set_value_sma10(self,valor):
        pass
    
    @abstractmethod
    def set_value_sma30(self, valor):
        pass
    
    @abstractmethod
    def generate_id(self):
        pass
    
    @abstractmethod
    def set_type(self, valor):
        pass
    
    @abstractmethod
    def set_current_date(self, date):
        pass
    
    @abstractmethod
    def set_current_date_general(self,date_general):
        pass
    
    @abstractmethod
    def set_current_date_manipulated(self,date_manipulated):
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def get_candles_data(self):
        pass

    @abstractmethod
    def removed_candle_last(self,candles):
        pass

    @abstractmethod
    def removed_candle_close(self,candles,amount):
        pass

    @abstractmethod
    def get_current_entrys(self,flash,smtp):
        pass

    @abstractmethod
    def get_rsi(self,candles,periodos):
        pass

    @abstractmethod
    def analized_rsi(self,candles):
        pass

    @abstractmethod
    def get_sma(self,candles,type_sma,account_candles):
        pass

    @abstractmethod
    def analized_sma(self,candles):
        pass

    @abstractmethod
    def get_indicators(self,result,candles):
        pass

    @abstractmethod
    def add_entry_platform(self, result):
        pass

    @abstractmethod
    def add_entry_traceability(self, result,id_cronjobs,smtp,result_candles):
        pass

    @abstractmethod
    def add_indicators(self,smtp,result_candles):
        pass

    @abstractmethod
    def add_movements(self,smtp,result_candles):
        pass

    @abstractmethod
    def add_result_entry(self,smtp):
        pass

    @abstractmethod
    def send_notification_telegram(self,result,telegram,id_cronjobs):
        pass

    @abstractmethod
    def add_result_entry_platform_v3(self,result):
        pass

    @abstractmethod
    def add_result_entry_platform_v2(self,result):
        pass

    @abstractmethod
    def add_result_entry_platform_v1(self,result):
        pass

    @abstractmethod
    def get_monetary_filter(self,result,smtp):
        pass

    @abstractmethod
    def get_par(self):
        pass

    @abstractmethod
    def set_par(self,valor):
        pass

    @abstractmethod
    def get_type_manager_day(self,day):
        pass

    @abstractmethod
    def set_mode(self,valor):
        pass

    @abstractmethod
    def get_mode(self):
        pass