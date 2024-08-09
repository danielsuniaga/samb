from decouple import config

class repositories_ligistic_regression():

    cursor_db = None

    sma10 = None

    sma30 = None

    rsi = None

    def __init__(self,cursor):

        self.cursor_db = cursor

        self.sma10 = config("SMA10")

        self.sma30 = config("SMA30")

        self.rsi = config("RSI10")

    def get_sma10(self): 

        return self.sma10
    
    def get_sma30(self):

        return self.sma30
    
    def get_rsi(self):

        return self.rsi

    def get_dataset_general_expansive(self):

        try:

            query = "WITH Last30Movements AS( SELECT samb_movements.id_entry_id, samb_movements.registration_date AS movement_registration_date, samb_movements.open_candle AS movement_open_candle, samb_movements.close_candle AS movement_close_candle, samb_movements.max_candle AS movement_high_candle, samb_movements.min_candle AS movement_low_candle, samb_movements.volume_candle AS movement_volume_candle, ROW_NUMBER() OVER(PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.registration_date DESC) AS rn FROM samb_movements) SELECT Last30Movements.id_entry_id AS id_entry_id, Last30Movements.rn AS num_candle, CASE WHEN samb_entrys.type = 'call' THEN 1 WHEN samb_entrys.type = 'put' THEN 0 ELSE NULL END AS entry_type, CASE WHEN samb_entrys.type_account = 'PRACTICE' THEN 0 WHEN samb_entrys.type_account = 'REAL' THEN 1 ELSE NULL END AS entry_type_account, samb_entrys.number_candle AS entry_number_candle, CASE WHEN samb_entrys.condition_entry = 'CLOSE' THEN 1 ELSE NULL END AS entry_condition, samb_entrys.amount AS entry_amount, samb_entrys.registration_date AS entry_registration_date, samb_entrys.condition AS entry_condition, CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result, sma_30.value AS sma_30_value, sma_10.value AS sma_10_value, rsi.value AS rsi_value, Last30Movements.movement_open_candle, Last30Movements.movement_close_candle, Last30Movements.movement_high_candle, Last30Movements.movement_low_candle, Last30Movements.movement_volume_candle FROM samb_entrys INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id INNER JOIN Last30Movements ON samb_entrys.id = Last30Movements.id_entry_id LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s WHERE Last30Movements.rn <= 30 AND samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id )"

            parameters = (self.get_sma30(),self.get_sma10(),self.get_rsi())

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "+str(err)}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}
    
    def get_dataset_general(self):

        try:

            query = "WITH Last30Movements AS( SELECT samb_movements.id_entry_id, samb_movements.registration_date AS movement_registration_date, samb_movements.open_candle AS movement_open_candle, samb_movements.close_candle AS movement_close_candle, samb_movements.max_candle AS movement_high_candle, samb_movements.min_candle AS movement_low_candle, samb_movements.volume_candle AS movement_volume_candle, ROW_NUMBER() OVER (PARTITION BY samb_movements.id_entry_id ORDER BY samb_movements.id_entity_candle DESC) AS rn FROM samb_movements) SELECT Last30Movements.id_entry_id AS id_entry_id, Last30Movements.rn AS num_candle, CASE WHEN samb_entrys.type = 'call' THEN 1 WHEN samb_entrys.type = 'put' THEN 0 ELSE NULL END AS entry_type, CASE WHEN samb_entrys.type_account = 'PRACTICE' THEN 0 WHEN samb_entrys.type_account = 'REAL' THEN 1 ELSE NULL END AS entry_type_account, samb_entrys.number_candle AS entry_number_candle, CASE WHEN samb_entrys.condition_entry = 'CLOSE' THEN 1 ELSE NULL END AS entry_condition, samb_entrys.amount AS entry_amount, samb_entrys.registration_date AS entry_registration_date, samb_entrys.condition AS entry_condition, CASE WHEN samb_entrys_results.result > 0 THEN 1 WHEN samb_entrys_results.result < 0 THEN 0 ELSE samb_entrys_results.result END AS entry_result, sma_30.value AS sma_30_value, sma_10.value AS sma_10_value, rsi.value AS rsi_value, Last30Movements.movement_open_candle, Last30Movements.movement_close_candle, Last30Movements.movement_high_candle, Last30Movements.movement_low_candle, Last30Movements.movement_volume_candle FROM samb_entrys INNER JOIN samb_entrys_results ON samb_entrys.id = samb_entrys_results.id_entrys_id INNER JOIN Last30Movements ON samb_entrys.id = Last30Movements.id_entry_id LEFT JOIN samb_indicators_entrys sma_30 ON sma_30.id_entry_id = samb_entrys.id AND sma_30.id_indicators_id = %s LEFT JOIN samb_indicators_entrys sma_10 ON sma_10.id_entry_id = samb_entrys.id AND sma_10.id_indicators_id = %s LEFT JOIN samb_indicators_entrys rsi ON rsi.id_entry_id = samb_entrys.id AND rsi.id_indicators_id = %s WHERE Last30Movements.rn <= 1 AND samb_entrys_results.registration_date = ( SELECT MAX(registration_date) FROM samb_entrys_results AS ser WHERE ser.id_entrys_id = samb_entrys.id ) ORDER BY samb_entrys.registration_date DESC"

            parameters = (self.get_sma30(),self.get_sma10(),self.get_rsi())

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "+str(err)}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}