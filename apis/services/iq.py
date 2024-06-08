import apis.repositories.iq as repository_iqs

from decouple import config
from iqoptionapi.stable_api import IQ_Option
from decimal import Decimal

import uuid
import time

class cases_iq:

    def __init__(self,cursor):

        self.username = config("USERNAME")

        self.password = config("PASSWORD")

        self.API = None

        self.mode = config("MODE")

        self.end_from_time = time.time()

        self.ANS=[]

        self.par=config("PAR")

        self.candles=config("CANDLE")

        self.candle_analized = int(config("CANDLE_ANALIZED"))

        self.candle_removed = int(config("CANDLE_REMOVED"))

        self.interval=config("INTERVAL")

        self.type = None

        self.number_loops = config("NUMBER_LOOPS")

        self.iq = repository_iqs.repositories_iq(cursor)

        self.current_date = None

        self.current_date_general = None

        self.current_date_manipulated = None

        self.minutes_manipulated = config("MINUTES")

        self.indicator = config("INDICATORS")

        self.candles_rsi = int(config("CANDLE_RSI"))

        self.type_rsi = int(config("TYPE_RSI"))

        self.min_rsi = int(config("RSI_MIN"))

        self.max_rsi =  int(config("RSI_MAX"))

        self.sma_short = int(config("SMA_SHORT"))

        self.sma_long = int(config("SMA_LONG"))

        self.candle_sma_short = int(config("CANDLE_SMA_SHORT"))

        self.candle_sma_long = int(config("CANDLE_SMA_LONG"))

        self.type_entry_short = config("TYPE_ENTRY_SHORT")

        self.type_entry_long = config("TYPE_ENTRY_LONG")

        self.candle_last = int(config("CANDLE_LAST"))

        self.last = int(config("LAST"))

        self.money = int(config("MONEY"))

        self.expirations_mode = int(config("EXPIRATIONS_MODE"))

        self.rsi=None

        self.sma10=None

        self.sma30=None

        self.rsi_id=config("RSI10")

        self.sma10_id=config("SMA10")

        self.sma30_id=config("SMA30")

        self.condition=config("CONDITION")

        self.message=None 

        self.message_entry_short=config("MESSAGE_ENTRY_SHORT")

        self.message_entry_long=config("MESSAGE_ENTRY_LONG")

        self.sleep = int(config("SLEEP"))

        self.active_rsi = int(config("ACTIVE_RSI"))

        self.active_sma = int(config("ACTIVE_SMA"))

        self.profit = int(config("PROFIT"))

        self.loss = int(config("LOSS"))

        self.project_name = config("PROJECT_NAME")

    def set_message(self,valor):

        self.message = valor

        return True

    def add_message_text(self,valor):

        self.message = self.message + " - "+valor

        return True

    def set_value_rsi(self,valor):

        self.rsi = valor

        return True

    def set_value_sma10(self,valor):

        self.sma10 = valor

        return True

    def set_value_sma30(self,valor):

        self.sma30 = valor

        return True

    def generate_id(self):

        return uuid.uuid4().hex
    
    def set_type(self,valor):

        self.type = valor

        return True

    def set_current_date(self, date):

        self.current_date = date

        return True

    def set_current_date_general(self, date_general):

        self.current_date_general = date_general

        return True

    def set_current_date_manipulated(self,date_manipulated):

        self.current_date_manipulated = date_manipulated

        return True

    def set_balance(self):

        try:

            self.API.change_balance(self.mode)

        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al posicionar el modo'+str(err)}
        
        return {'status':True,'msj':'Success'}

    def check(self):

        try:

            return {'status':True,'msj':'Success sync'} if self.API.check_connect() else {'status':False,'msj': "Error al conectar con IQ Option"}

        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al chequear sincronizcion con iq'+str(err)}

    def init(self):

        try:

            self.API = IQ_Option(self.username, self.password)

            self.API.connect()

        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al sincronizarnos con iq'+str(err)}

        return self.check()
    
    def get_candles_data(self):
    
        _end_from_time=time.time()

        for _ in range(1):

            _data=self.API.get_candles(self.par, int(self.interval), int(self.candles), _end_from_time)
            
            self.ANS =_data+self.ANS

            _end_from_time=int(_data[0]["from"])-1
        
        return self.ANS
    
    def removed_candle_last(self,candles):

        candles.pop()

        return candles

    def removed_candle_close(self,candles,amount):

        total_length = len(candles)

        close_prices = [Decimal(candles[i]["close"]) for i in range(total_length - amount, total_length)]

        close_prices = self.removed_candle_last(close_prices)

        return close_prices
    
    def analized_candles(self, candles):

        candles = self.removed_candle_close(candles,self.candle_removed)

        if all(candles[i] < candles[i+1] for i in range(self.candle_analized - 1)):

            self.set_type(self.type_entry_long)

            self.set_message(self.mode+" - "+self.project_name+" - "+self.message_entry_long+" - "+self.par)

            # ALCISTA
            return self.type_entry_long
        
        if all(candles[i] > candles[i+1] for i in range(self.candle_analized - 1)):

            self.set_type(self.type_entry_short)

            self.set_message(self.mode+" - "+self.project_name+" - "+self.message_entry_short+" - "+self.par)

            # BAJISTA
            return self.type_entry_short
        
        return 0
    
    def get_current_entrys(self,flash,smtp):

        if flash==self.type_entry_long or flash==self.type_entry_short:

            result=self.iq.get_current_entrys(self.current_date)

            if not result['status']:

                smtp.send_notification_email(self.current_date_general, result['msj'])

                return False
            
            result=self.iq.get_current_entrys_min(self.current_date_manipulated,self.candles)

            if not result['status']:

                smtp.send_notification_email(self.current_date_general, result['msj'])

                return False
            
            return True
        
        return False
    
    def get_rsi(self,candles,periodos):

        gains = []

        losses = []

        # Calcular cambios en los precios y clasificar en ganancias y pérdidas
        for i in range(1, len(candles)):

            change = Decimal(candles[i]) - Decimal(candles[i - 1])

            if change > 0:

                gains.append(change)

                losses.append(0)

            elif change < 0:

                gains.append(0)

                losses.append(-change)

            else:

                gains.append(0)

                losses.append(0)

        avg_gain = sum(gains) / periodos  # Promedio de ganancias en los últimos 10 períodos

        avg_loss = sum(losses) / periodos  # Promedio de pérdidas en los últimos 10 períodos

        # Evitar división por cero
        if avg_loss == 0:

            return 100

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi
    
    def analized_rsi(self,candles):

        local_candles = self.removed_candle_close(candles,self.candles_rsi)

        result = self.get_rsi(local_candles,self.type_rsi)

        self.set_value_rsi(result)

        if((self.min_rsi<Decimal(result)) and (Decimal(result)<self.max_rsi)):

            return True

        return False
    
    def get_sma(self,candles,type_sma,account_candles):

        local_candles = self.removed_candle_close(candles,account_candles)

        sma = sum(local_candles[-type_sma:]) / type_sma
        
        return sma
    
    def analized_sma(self,candles):

        result_sma_short = self.get_sma(candles,self.sma_short,self.candle_sma_short)

        self.set_value_sma10(result_sma_short)

        result_sma_long = self.get_sma(candles,self.sma_long,self.candle_sma_long)

        self.set_value_sma30(result_sma_long)

        local_candles = self.removed_candle_close(candles,self.candle_last)

        if(self.type==self.type_entry_short) and ((Decimal(result_sma_short)>Decimal(local_candles[self.last])) and (Decimal(result_sma_long)>Decimal(local_candles[self.last]))):

            return True
        
        if(self.type==self.type_entry_long) and ((Decimal(result_sma_short)<Decimal(local_candles[self.last])) and (Decimal(result_sma_long)<Decimal(local_candles[self.last]))):

            return True

        return False
    
    def get_indicators(self,result,candles):

        if not result:

            return False

        result_rsi = self.analized_rsi(candles)

        result_sma = self.analized_sma(candles)

        if self.active_rsi and self.active_sma:

            return result_rsi and result_sma
        
        if self.active_rsi:

            return result_rsi
        
        if self.active_sma:

            return result_sma

        return True

    def add_entry_platform(self, result):

        if not result:

            return False

        check,id_entry=self.API.buy(self.money,self.par,self.type,self.expirations_mode)

        return id_entry if check else check
    
    def add_entry_traceability(self, result,id_cronjobs,smtp,result_candles):

        if not result:

            return False

        id_entry=self.generate_id()

        self.iq.set_id_entry(id_entry)

        result_entry = self.add_result_entry_platform_v3(result)

        self.iq.set_result_entry(result_entry)

        result_entry = "("+str(result_entry)+")"

        self.add_message_text(result_entry)

        result=self.iq.add_entrys(self.current_date_general,id_cronjobs,self.type,result)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False
        
        return self.add_indicators(smtp,result_candles)

    def add_indicators(self,smtp,result_candles):

        result=self.iq.add_indicators(self.generate_id(),self.current_date_general,self.rsi_id,self.rsi)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False
                    
        result=self.iq.add_indicators(self.generate_id(),self.current_date_general,self.sma10_id,self.sma10)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False
        
        result=self.iq.add_indicators(self.generate_id(),self.current_date_general,self.sma30_id,self.sma30)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False

        return self.add_movements(smtp,result_candles)
    
    def add_movements(self,smtp,result_candles):

        # Preparar los datos para la inserción en lote
        data_to_insert = [(self.generate_id(),self.current_date_general,self.current_date_general,self.condition,candle["at"], candle["close"], candle["from"], candle["id"], self.iq.get_id_entry(), candle["max"], candle["min"], candle["open"], candle["to"], candle["volume"]) for candle in result_candles]

        result=self.iq.add_movements(data_to_insert)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False
        
        return self.add_result_entry(smtp)
    
    def add_result_entry(self,smtp):

        id_entry_result=self.generate_id()

        result=self.iq.add_entrys_result(id_entry_result,self.current_date_general)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

            return False
        
        return True
    
    def send_notification_telegram(self,result,telegram,id_cronjobs):

        if not result:

            return False

        return telegram.send(self.message,id_cronjobs,self.current_date_general)
            
    def add_result_entry_platform_v3(self,result):

        return self.API.check_win_v3(result)
    
    def add_result_entry_platform_v2(self,result):

        polling_time=3

        return self.API.check_win_v2(result,polling_time)
    
    def add_result_entry_platform_v1(self,result):

        return self.API.check_win(result)
    
    def add_result_entry_traceability(self, result):
    
        if(result):

            result = self.add_result_entry_v3(result)
        
    def get_monetary_filter(self,result,smtp):

        if not result:

            return False
        
        result = self.iq.get_sum_entrys_date(self.current_date)

        if not result['status']:

            smtp.send_notification_email(self.current_date_general, result['msj'])

        if(result['data'] >= self.profit) or (result['data'] <= self.loss):

            return False

        return True
        

    def get_par(self):

        return self.par
    
    def set_par(self,valor):

        self.par = valor

        return True
    
    def analized_day(self,date):

        result = date.get_day()

        if(result<5):

            return False
        
        return True
    
    def set_asset_financial(self,date):

        if self.analized_day(date):

            return self.set_par(self.get_par()+'-OTC')

        return True
    
    def get_loops(self,date,smtp,id_cronjobs,telegram):

        self.set_asset_financial(date)
    
        for _ in range(int(self.number_loops)):

            now = date.get_current_utc5()

            current_date_local = date.get_current_date(now)

            self.set_current_date(date.get_current_date_only(now))

            self.set_current_date_general(current_date_local)

            self.set_current_date_manipulated(date.get_current_date(date.get_current_date_minus_minutes(now,int(self.minutes_manipulated))))

            result_candles = self.get_candles_data()

            result = self.analized_candles(result_candles)

            result = self.get_current_entrys(result,smtp)

            result = self.get_indicators(result,result_candles)

            result = self.get_monetary_filter(result,smtp)

            result = self.add_entry_platform(result)

            result = self.add_entry_traceability(result,id_cronjobs,smtp,result_candles)

            self.send_notification_telegram(result,telegram,id_cronjobs)

            if not result:

                time.sleep(self.sleep)

            else:

                break

        return True
