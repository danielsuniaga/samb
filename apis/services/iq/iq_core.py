from decouple import config

from iqoptionapi.stable_api import IQ_Option

from decimal import Decimal

from apis.services.iq.iiq_core import icases_iq_core

import uuid

import time
class cases_iq_core(icases_iq_core):

    iq = None

    API = None

    regression_logistic_model_general = None

    id_predict_model_general_repository = None

    id_entry_service = None

    type=None

    message=None

    rsi=None 

    sma10=None

    sma30=None

    current_date = None

    current_date_general = None

    current_date_manipulated = None

    events = None

    config = None

    nomenclature_par_otc = None

    nomenclature_par_op = None

    def __init__(self,cursor):


        self.username = config("USERNAME")

        self.password = config("PASSWORD")

        self.par=config("PAR").strip()

        self.interval=config("INTERVAL")

        self.candles=config("CANDLE")

        self.ANS=[]

        self.candle_removed = int(config("CANDLE_REMOVED"))

        self.candle_analized = int(config("CANDLE_ANALIZED"))

        self.type_entry_long = config("TYPE_ENTRY_LONG")

        self.mode = config("MODE")

        self.mode_basic = config("MODE")

        self.project_name = config("PROJECT_NAME")

        self.message_entry_long=config("MESSAGE_ENTRY_LONG")

        self.type_entry_short = config("TYPE_ENTRY_SHORT")

        self.message_entry_short=config("MESSAGE_ENTRY_SHORT")

        self.candles_rsi = int(config("CANDLE_RSI"))

        self.type_rsi = int(config("TYPE_RSI"))

        self.min_rsi = int(config("RSI_MIN"))

        self.max_rsi =  int(config("RSI_MAX"))

        self.sma_short = int(config("SMA_SHORT"))

        self.candle_sma_short = int(config("CANDLE_SMA_SHORT"))

        self.sma_long = int(config("SMA_LONG"))

        self.candle_sma_long = int(config("CANDLE_SMA_LONG"))

        self.candle_last = int(config("CANDLE_LAST"))

        self.end_from_time = time.time()

        self.number_loops = config("NUMBER_LOOPS")

        self.minutes_manipulated = config("MINUTES")

        self.indicator = config("INDICATORS")

        self.last = int(config("LAST"))

        self.money = int(config("MONEY"))

        self.expirations_mode = int(config("EXPIRATIONS_MODE"))

        self.rsi_id=config("RSI10")

        self.sma10_id=config("SMA10")

        self.sma30_id=config("SMA30")

        self.condition=config("CONDITION")

        self.sleep = int(config("SLEEP"))

        self.active_rsi = int(config("ACTIVE_RSI"))

        self.active_sma = int(config("ACTIVE_SMA"))

        self.profit = int(config("PROFIT"))

        self.loss = int(config("LOSS"))

        self.nomenclature_par_otc = config("NOMENCLATURE_PAR_OTC")

        self.nomenclature_par_op = config("NOMENCLATURE_PAR_OP")

    def init_config(self,value):

        self.config = value

        return True
    
    def get_nomenclature_par_otc(self):

        return self.nomenclature_par_otc
    
    def get_nomenclature_par_op(self):

        return self.nomenclature_par_op

    def get_project_name(self):

        return self.project_name
    
    def init_events(self,value):

        self.events = value
        
        return True
    
    def set_events_field(self,field,value):

        return self.events.set_events_field(field,value)
    
    def get_events(self):

        return self.events.get_events()
    
    def generate_msj_events(self):

        return self.events.generate_msj_events()
    
    def get_message(self):

        return self.message
    
    def set_id_entry_services(self,value):

        self.id_entry_service = value

        return True
    
    def get_id_entry_services(self):

        return self.id_entry_service
    
    def get_candle_analized(self):

        return self.candle_analized
    
    def get_mode_basic(self):

        return self.mode_basic
    
    def get_type_entry_short(self):

        return self.type_entry_short
    
    def set_id_predict_model_general_repository(self,value):

        self.id_predict_model_general_repository = value

        return True
    
    def get_id_predict_model_general_repository(self):

        return self.id_predict_model_general_repository

    def get_type(self):
        
        return self.type

    def init_regression_logistic_model_general(self,value):

        self.regression_logistic_model_general = value

        return True
    
    def set_loss(self,valor):

        self.loss = int(valor)

        return True
    
    def get_loss(self):

        return self.loss

    def set_profit(self,valor):

        self.profit = int(valor)

        return True

    def get_profit(self):

        return self.profit

    def set_money(self,valor):

        self.money = int(valor)

        return True
    
    def get_money(self):

        return self.money

    def set_message(self,valor):

        self.message = valor

        return True
    
    def add_message(self,valor):

        self.message = self.message +str(valor)

        return True
    
    def add_message_text(self,valor):

        self.message = self.message + " - "+valor

        return True
    
    def set_value_rsi(self,valor):

        self.rsi = valor

        return True
    
    def get_value_rsi(self):

        return self.rsi
    
    def set_value_sma10(self,valor):

        self.sma10 = valor

        return True
    
    def get_value_sma10(self):
        
        return self.sma10
    
    def set_value_sma30(self,valor):

        self.sma30 = valor

        return True
    
    def get_value_sma30(self):

        return self.sma30
    
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
    
    def check(self):

        try:

            return {'status':True,'msj':'Success sync'} if self.API.check_connect() else {'status':False,'msj': "Error al conectar con IQ Option"}

        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al chequear sincronizcion con iq'+str(err)}
        
    def set_config_open_otc(self,value):

        return self.config.set_config_open_otc(value)
    
    def check_active_access(self):

        par_services = self.get_par()

        all_open_time = self.API.get_all_open_time()
        
        if 'binary' not in all_open_time:

            return par_services+" no se encuentra en ningún formato conocido. "

        binary_pairs = all_open_time['binary']

        if not par_services in binary_pairs:
            
            return par_services+" no se encuentra el activo financiero enlistado. "
            
        return self.check_market_status(binary_pairs, par_services)

    def check_market_status(self, binary_pairs, par_services):

        nominal_status = self.check_nominal_market(binary_pairs, par_services)

        otc_status = self.check_otc_market(binary_pairs, par_services)

        op_status = self.check_op_market(binary_pairs, par_services)

        return nominal_status+otc_status+op_status
    
    def set_config_open_nom(self,value):

        return self.config.set_config_open_nom(value)
    
    def set_config_open_otc(self,value):

        return self.config.set_config_open_otc(value)
    
    def set_config_open_ope(self,value):

        return self.config.set_config_open_ope(value)

    def check_nominal_market(self, binary_pairs, par):

        if par in binary_pairs and binary_pairs[par]["open"]:

            self.set_config_open_nom(1)

            return par+" está activo en nominal. "
        
        self.set_config_open_nom(0)

        return par+" está no activo en nominal. "

    def check_otc_market(self, binary_pairs, par):

        otc_format = par + self.get_nomenclature_par_otc()

        if otc_format in binary_pairs and binary_pairs[otc_format]["open"]:

            self.set_config_open_otc(1)

            return par+" está activo en OTC. "
        
        self.set_config_open_otc(0)

        return par+" está no activo en OTC. "

    def check_op_market(self, binary_pairs, par):

        op_format = par + self.get_nomenclature_par_op()

        if op_format in binary_pairs and binary_pairs[op_format]["open"]:
            
            self.set_config_open_ope(1)

            return par+" está activo en OP. "
        
        self.set_config_open_ope(0)

        return par+" está no activo en OP. "
        
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

        self.set_id_entry_services(id_entry)

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
        
        return self.add_entry_predict_model_general_logistic_regression()
        
    def add_entry_predict_model_general_logistic_regression(self):

        if not self.check_active_model_general():

            return True

        return self.regression_logistic_model_general.add_entry_predict_model_general_logistic_regression(self.get_id_predict_model_general_repository(),self.get_id_entry_services())
    
    def get_messsage_default_services_model_general(self):

        return self.regression_logistic_model_general.get_message_default_services()
    
    def get_message_model_general_logistic_regression(self):

        if not self.check_active_model_general():

            return self.get_messsage_default_services_model_general()

        return self.regression_logistic_model_general.get_message_user()
    
    def send_msj_telegram(self,msj):
        
        self.telegram.send_without_persistence(msj)

        return True
    
    def send_notification_telegram(self,result,telegram,id_cronjobs):

        if not result:

            return False

        return telegram.send(self.get_message()+self.get_message_model_general_logistic_regression()+self.generate_msj_events(),id_cronjobs,self.current_date_general)
            
    def add_result_entry_platform_v3(self,result):

        return self.API.check_win_v3(result)
    
    def add_result_entry_platform_v2(self,result):

        polling_time=3

        return self.API.check_win_v2(result,polling_time)
    
    def add_result_entry_platform_v1(self,result):

        return self.API.check_win(result)
        
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
    
    def get_type_manager_day(self,day):

        result = self.iq.get_type_manager_day(day)

        if not result['status']: 

            return False

        return result['data']
    
    def set_mode(self,valor):

        self.mode = valor

        return True
    
    def get_mode(self):

        return self.mode
    
    def get_entry_type(self):

        if self.get_type() == self.get_type_entry_short():

            return 0

        return 1
    
    def get_entry_type_account(self):

        if self.get_mode() == self.get_mode_basic():

            return 0
        
        return 1
    
    def get_entry_condition_data(self):

        return 1
    
    def generate_candles_sort_reversed(self,candles):

        return sorted(candles,key=lambda x: x['id'],reverse=True)
    
    def get_candles_first(self,candles):

        return candles[0]
    
    def get_current_date_specific(self,dates,specific):

        now = dates.get_current_utc5()

        return int(dates.get_current_date_specific(now,specific))
    
    def init_data_get_regression_logistic_model_general(self,candles,dates):

        candles_sorted = self.get_candles_first(self.generate_candles_sort_reversed(candles))

        return {
            "entry_type": self.get_entry_type(),
            "entry_type_account": self.get_entry_type_account(),
            "entry_number_candle": self.get_candle_analized(),
            "entry_condition": self.get_entry_condition_data(),
            "entry_amount": self.get_money(),
            "sma_30_value": self.get_value_sma30(),
            "sma_10_value": self.get_value_sma10(),
            "rsi_value": self.get_value_rsi(),
            "movement_open_candle": candles_sorted['open'],
            "movement_close_candle": candles_sorted['close'],
            "movement_high_candle": candles_sorted['max'],
            "movement_low_candle": candles_sorted['min'],
            "movement_volume_candle": candles_sorted['volume'],
            "year": self.get_current_date_specific(dates,'%Y'),
            "month": self.get_current_date_specific(dates,'%m'),
            "day": self.get_current_date_specific(dates,'%d'),
            "hour": self.get_current_date_specific(dates,'%H'),
            "minute": self.get_current_date_specific(dates,'%M'),
            "second": self.get_current_date_specific(dates,'%S')
        }
    
    def get_position_prediction(self,candles,date):

        data = self.init_data_get_regression_logistic_model_general(candles,date)
            
        return self.regression_logistic_model_general.get_position_prediction(data)
    
    def check_active_model_general(self):

        return self.regression_logistic_model_general.check_active_general()
    
    def get_regression_logistic_model_general(self,result,candles,date):
        
        if not result:

            return False
        
        if not self.check_active_model_general():

            return True
                
        id_samb_predict_model_general_logistic_regression = self.get_position_prediction(candles,date)

        if not id_samb_predict_model_general_logistic_regression:

            return id_samb_predict_model_general_logistic_regression
                
        self.set_id_predict_model_general_repository(id_samb_predict_model_general_logistic_regression)

        return self.get_id_predict_model_general_repository()
