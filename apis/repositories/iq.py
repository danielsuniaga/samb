from decouple import config

class repositories_iq:

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.count = None

        self.condition = config("CONDITION")

        self.start_date = config("START")

        self.end_date = config("END")

        self.max_entry = config("MAX_ENTRY")

        self.min_entry = config("MIN_ENTRY")

        self.mode = config("MODE")

        self.candle_analized = config("CANDLE_ANALIZED")

        self.condition_entry = config("CONDITION_ENTRY")

        self.amount = config("MONEY")

        self.id_entry=None

        self.result_entry = None

        self.result_operation=config("RESULT_OPERATION")

    def set_result_entry(self,valor):

        self.result_entry = valor

    def get_result_entry(self):

        return self.result_entry

    def get_id_entry(self):

        return self.id_entry

    def set_id_entry(self,valor):
    
        self.id_entry = valor
        
    def set_complement_start_date(self,date):

        self.start_date = str(date) + self.start_date

    def set_complement_end_date(self,date):

        self.end_date = str(date) + self.end_date

    def seteo_count(self):

        self.count = None

    def get_current_entrys(self,date):

        self.set_complement_start_date(date)

        self.set_complement_end_date(date)

        try:

            self.count=self.cursor_db.execute("SELECT samb_entrys.id AS id FROM samb_entrys WHERE samb_entrys.CONDITION=%s AND samb_entrys.registration_date>%s AND samb_entrys.registration_date<%s",[self.condition,self.start_date,self.end_date])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las entrys escritas  "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count<int(self.max_entry) else {'status':False,'msj': "Cantidad maxima alcanzada"}
    
    def get_current_entrys_min(self,date,candles):

        self.seteo_count()

        try:

            self.count=self.cursor_db.execute("SELECT samb_entrys.id AS id FROM samb_entrys WHERE samb_entrys.CONDITION=%s AND samb_entrys.registration_date>%s AND samb_entrys.number_candle=%s LIMIT 1",[self.condition,date,candles])
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las entrys escritas  "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count<int(self.min_entry) else {'status':False,'msj': "Cantidad maxima alcanzada en 5 minutos"}
    
    def add_entrys(self,current_date,id_cronjobs,type_operations,id_entry_platform):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys(samb_entrys.id,samb_entrys.type,samb_entrys.type_account,samb_entrys.number_candle,samb_entrys.condition_entry,samb_entrys.amount,samb_entrys.registration_date,samb_entrys.update_date,samb_entrys.condition,samb_entrys.id_samb_cronjobs_id,samb_entrys.id_entry_platform,samb_entrys.result_platform)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[self.id_entry,type_operations,self.mode,self.candle_analized,self.condition_entry,self.amount,current_date,current_date,self.condition,id_cronjobs,id_entry_platform,self.result_operation])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def add_entrys_result(self,id_entry_result,current_date):

        try:

            self.cursor_db.execute("INSERT INTO samb_entrys_results(samb_entrys_results.id,samb_entrys_results.result,samb_entrys_results.registration_date,samb_entrys_results.update_date,samb_entrys_results.condition,samb_entrys_results.id_entrys_id)VALUES(%s,%s,%s,%s,%s,%s)",[id_entry_result,self.result_entry,current_date,current_date,self.condition,self.id_entry])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_entrys_results '+str(err)}
        
        return {'status':True,'msj':'Success'}
    
    def add_indicators(self,id_tuple,current_date,id_indicators,value_indicators):
        
        try:

            self.cursor_db.execute("INSERT INTO samb_indicators_entrys(samb_indicators_entrys.id,samb_indicators_entrys.registration_date,samb_indicators_entrys.condition,samb_indicators_entrys.id_entry_id,samb_indicators_entrys.id_indicators_id,samb_indicators_entrys.value)VALUES(%s,%s,%s,%s,%s,%s)",[id_tuple,current_date,self.condition,self.id_entry,id_indicators,value_indicators])

        except Exception as err:

            return {'status': False, 'msj':'No se realizo la escritura en samb_indicators_entrys'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def add_movements(self,candles):

        try:

            self.cursor_db.executemany("INSERT INTO samb_movements(samb_movements.id,samb_movements.registration_date,samb_movements.update_date,samb_movements.condition,samb_movements.at_candle,samb_movements.close_candle,samb_movements.from_candle,samb_movements.id_entity_candle,samb_movements.id_entry_id,samb_movements.max_candle,samb_movements.min_candle,samb_movements.open_candle,samb_movements.to_candle,samb_movements.volume_candle)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",candles)

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_movements '+str(err)}

        return {'status':True,'msj':'Success'}
    
    def get_sum_entrys_date(self,date):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results WHERE date_format(samb_entrys_results.registration_date, %s) = %s"

            self.cursor_db.execute(query, ('%Y%m%d', date))

            result = self.cursor_db.fetchone() 
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_entrys_results leidas  "+str(err)}
        
        return {'status':True,'data':result[0],'msj':'Success'}

