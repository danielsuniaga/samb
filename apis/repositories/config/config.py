class repositories_config:

    cursor = None

    def __init__(self,cursor):

        self.cursor = cursor

    def set_config(self,id,value):

        try:

            self.cursor.execute("UPDATE samb_config SET samb_config.value = %s WHERE samb_config.id = %s",[value,id])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_config'+str(err)}

        return {'status':True,'msj':'Success'}
    
    def get_config(self,id):

        try:

            query = "SELECT samb_config.value FROM samb_config WHERE samb_config.id = %s"

            parameters = (id)

            self.cursor.execute(query,parameters)

            result = self.cursor.fetchall()

            column_names = [desc[0] for desc in self.cursor.description]

            result_with_columns = [dict(zip(column_names, row)) for row in result]
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de samb_config  "+str(err)}
                
        return {'status':True,'data':result_with_columns[0],'msj':'Success'}