import apis.repositories.notification as repository_notifications

from apis.services.ismtp import icases_smtp

from decouple import config

class cases_smtp(icases_smtp):

    def __init__(self,cursor):

        self.smtp = repository_notifications.repositories_smtp(cursor)

        self.start_date = config("START")

        self.end_date = config("END")

        self.start_date_another = config("START_ANOTHER")

        self.end_date_another = config("END_ANOTHER")

        self.subject_reports_nominal = "Management report ("+config("PROJECT_NAME")+") SESSION NOMINAL | SAMB | TRADING "

        self.subject_reports_another = "Management report ("+config("PROJECT_NAME")+") SESSION ANOTHER | SAMB | TRADING "

    def get_subject_reports_nominal(self):

        return self.subject_reports_nominal
    
    def get_subject_reports_another(self):

        return self.subject_reports_another
    
    def set_subject_reports(self,valor):

        self.smtp.set_subject_reports(valor)

        return True

    def get_end_date_another(self):

        return self.end_date_another
    
    def get_start_date_another(self):

        return self.start_date_another

    def get_end_date(self):

        return self.end_date
    
    def get_start_date(self):

        return self.start_date

    def set_end_date_repository(self,valor):

        self.smtp.set_end_date(valor)

        return True
    
    def set_start_date_repository(self,valor):

        self.smtp.set_start_date(valor)

        return True

    def send_notification_email(self,date,mensaje):
        
        return self.smtp.send(date,mensaje)
    
    def send_reporting_email(self,date):
            
        return self.smtp.send_reports(date,self.data_reporting())
    
    def get_data_repository(self,mode,day):

        if(day==0):

            return self.smtp.get_data_reporting_cur(mode)
        
        if(day==9):

            return self.smtp.get_data_reporting_tot(mode)

        return self.smtp.get_data_reporting(mode,day)
    
    def structure_registry_data(self,data):

        return {"day": data['name'], "demo": self.get_data_repository("PRACTICE",data['database']), "real": self.get_data_repository("REAL",data['database'])}
    
    def init_data_days(self):

        return [
            
            {"name":"Actually","database":0},
            {"name":"Monday","database":2},
            {"name":"Tuesday","database":3},
            {"name":"Wednesday","database":4},
            {"name":"Thursday","database":5},
            {"name":"Friday","database":6},
            {"name":"Saturday","database":7},
            {"name":"Sunday","database":1},
            {"name":"Total","database":9}

        ]

    def init_data_reporting(self):

        dias = self.init_data_days()

        result = []

        for registro in dias:

            result.append(self.structure_registry_data(registro))

        return result              
    
    def get_format_data_reporting(self,registro):

        return """ <tr><td>"""+str(registro["day"])+"""</td><td>"""+str(registro["demo"])+"""</td><td>"""+str(registro["real"])+"""</td></tr> """

    def get_data_reporting(self,data):

        result = ""

        for registro in data:

            result += self.get_format_data_reporting(registro)

        return result

    def data_reporting(self):

        result = self.init_data_reporting()

        return self.get_data_reporting(result)