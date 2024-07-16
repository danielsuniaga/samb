from decouple import config

from apis.repositories.iq.iq_core import repositories_iq_core

from apis.repositories.iq.iiq import irepositories_iq

class repositories_iq(repositories_iq_core,irepositories_iq):

    def __init__(self,cursor):

        super().__init__(cursor)

        self.start_date = config("START")

        self.end_date = config("END")
        
    def set_complement_start_date(self,date):

        self.start_date = str(date) + self.start_date

        return True

    def set_complement_end_date(self,date):

        self.end_date = str(date) + self.end_date

        return True

    def get_current_entrys(self,date):

        self.set_complement_start_date(date)

        self.set_complement_end_date(date)

        try:

            self.count=self.cursor_db.execute("SELECT samb_entrys.id AS id FROM samb_entrys WHERE samb_entrys.CONDITION=%s AND samb_entrys.registration_date>%s AND samb_entrys.registration_date<%s",[self.condition,self.start_date,self.end_date])

        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las entrys escritas  "+str(err)}
        
        return {'status':True,'msj':'Success'} if self.count<int(self.max_entry) else {'status':False,'msj': "Cantidad maxima alcanzada"}
    
    def get_sum_entrys_date(self,date):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results WHERE date_format(samb_entrys_results.registration_date, %s) = %s"

            self.cursor_db.execute(query, ('%Y%m%d', date))

            result = self.cursor_db.fetchone() 
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_entrys_results leidas  "+str(err)}
        
        return {'status':True,'data':result[0],'msj':'Success'}
    
    def get_type_manager_day(self,day):

        try:

            query = "SELECT samb_manager_days.type AS type FROM samb_manager_days WHERE samb_manager_days.day_number = %s"

            self.cursor_db.execute(query, day)

            result = self.cursor_db.fetchone() 
            
        except Exception as err:

            return {'status':False,'msj':"Incidencia en la lectura de las samb_manager_days leidas  "+str(err)}
                
        return {'status':True,'data':result[0],'msj':'Success'}



