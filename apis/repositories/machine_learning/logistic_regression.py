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

    def get_dataset_general(self):

        try:

            query = "x"

            parameters = (self.get_sma30(),self.get_sma10(),self.get_rsi())

            self.cursor_db.execute(query,parameters)

            result = self.cursor_db.fetchall()

            column_names = [desc[0] for desc in self.cursor_db.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de los datos necesarios para crear el dataset  "+str(err)}
                
        return {'status':True,'data':result_with_columns,'msj':'Success'}