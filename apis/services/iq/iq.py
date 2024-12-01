import apis.repositories.iq.iq as repository_iqs

from apis.services.iq.iq_core import cases_iq_core

import time

from apis.services.iq.iiq import icases_iq
class cases_iq(cases_iq_core,icases_iq):

    def __init__(self,cursor):

        super().__init__(cursor)

        self.iq = repository_iqs.repositories_iq(cursor)

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
    
    def analized_mode(self,date):

        result = self.get_type_manager_day(date.get_day())

        if not result: 

            return False
        
        self.set_mode(result['type'])

        self.set_money(result['money'])

        self.set_profit(result['profit'])

        self.set_loss(result['loss'])

        self.iq.set_mode(result['type'])

        self.iq.set_amount(result['money'])

        return True

    def set_balance(self,dates):

        self.analized_mode(dates)

        try:

            self.API.change_balance(self.mode)

        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al posicionar el modo'+str(err)}
        
        return {'status':True,'msj':'Success'}
    
    def analized_day(self,date):

        result = date.get_day()

        if(result<5):

            return False
        
        return True
    
    def check_market_type(self):

        return self.config.check_market()
    
    def check_par(self,value):

        return value.strip()
    
    def set_asset_financial(self):

        market_type = self.check_market_type()

        if not market_type:

            return False
        
        result = self.get_par()+market_type

        return self.set_par(self.check_par(result))

    def get_loops(self,date,smtp,id_cronjobs,telegram):

        self.set_asset_financial()
    
        for _ in range(int(self.number_loops)):

            self.set_events_field('init_loop',date.get_current_date_mil_dynamic())

            now = date.get_current_utc5()

            current_date_local = date.get_current_date(now)

            self.set_current_date(date.get_current_date_only(now))

            self.set_current_date_general(current_date_local)

            self.set_current_date_manipulated(date.get_current_date(date.get_current_date_minus_minutes(now,int(self.minutes_manipulated))))

            result_candles = self.get_candles_data()

            self.set_events_field('get_candles',date.get_current_date_mil_dynamic())

            result = self.analized_candles(result_candles)

            self.set_events_field('analized_candles',date.get_current_date_mil_dynamic())

            result = self.get_current_entrys(result,smtp)

            self.set_events_field('filter_current',date.get_current_date_mil_dynamic())
            
            result = self.get_indicators(result,result_candles)

            self.set_events_field('generate_indicators',date.get_current_date_mil_dynamic())

            result = self.get_monetary_filter(result,smtp)

            self.set_events_field('get_filter_monetary',date.get_current_date_mil_dynamic())

            result = self.get_regression_logistic_model_general(result,result_candles,date)

            self.set_events_field('get_model_general_rl',date.get_current_date_mil_dynamic())

            result = self.add_entry_platform(result)

            self.set_events_field('add_positions_brokers',date.get_current_date_mil_dynamic())

            result = self.add_entry_traceability(result,id_cronjobs,smtp,result_candles)

            self.set_events_field('add_persistence',date.get_current_date_mil_dynamic())

            self.send_notification_telegram(result,telegram,id_cronjobs)

            if not result:

                time.sleep(self.sleep)

            else:

                break

        return True
