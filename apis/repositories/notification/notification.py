from email import message

from decouple import config

import uuid

import smtplib

import email.message

import requests

from apis.repositories.notification.inotification import irepositories_notifications

from apis.repositories.notification.ismtp import irepositories_smtp

from apis.repositories.notification.itelegram import irepositories_telegram

class repositories_notifications(irepositories_notifications):

    def __init__(self,cursor):

        self.fecha = None

        self.cursor_db = cursor

        self.id_exceptions_api = config("ID_EXCEPTIONS_API")

        self.type_notification_telegram = config("TYPE_NOTIFICATION_TELEGRAM")

        self.chat = config("CHAT_ID")

        self.condition = config("CONDITION")

        self.start_date = config("START")

        self.end_date = config("END")

    def set_start_date(self,valor):
        
        self.start_date = valor

        return True

    def set_end_date(self,valor):

        self.end_date = valor

        return True

    def add_notificacion_exc(self,mensaje):

        try:

            self.cursor_db.execute("INSERT INTO samb_notifications_exceptions_apis_independient(samb_notifications_exceptions_apis_independient.id,samb_notifications_exceptions_apis_independient.description, samb_notifications_exceptions_apis_independient.registration_date,samb_notifications_exceptions_apis_independient.update_date,samb_notifications_exceptions_apis_independient.condition, samb_notifications_exceptions_apis_independient.id_exceptions_api_id)VALUES(%s,%s,%s,%s,%s,%s)",[uuid.uuid4().hex, mensaje, self.fecha, self.fecha, "1", self.id_exceptions_api])

        except Exception:

            return False

        return True  
    
    def add_reports(self):

        try:

            self.cursor_db.execute("INSERT INTO samb_reports(samb_reports.id,samb_reports.description,samb_reports.registration_date,samb_reports.update_date,samb_reports.state)VALUES(%s,%s,%s,%s,%s)",[uuid.uuid4().hex, "SEND REPORTS", self.fecha, self.fecha, "1"])

        except Exception:

            return False

        return True  
    
    def removed_special_characters(self,value):

        return str(value.replace("'", '').replace('"', ''))

    def add_notification_telegram(self,mensaje,response,id_cronjobs):

        try:

            self.cursor_db.execute("INSERT INTO samb_send_message_api_telegram(samb_send_message_api_telegram.id,samb_send_message_api_telegram.type,samb_send_message_api_telegram.message,samb_send_message_api_telegram.chat,samb_send_message_api_telegram.response_method,samb_send_message_api_telegram.registration_date,samb_send_message_api_telegram.update_date,samb_send_message_api_telegram.condition,samb_send_message_api_telegram.id_cronjobs_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[uuid.uuid4().hex, self.type_notification_telegram, mensaje, self.chat,response,self.fecha, self.fecha, self.condition, id_cronjobs])

        except Exception as err:

            return {'status': False, 'message':'No se realizo la escritura en samb_send_message_api_telegram: '+str(err)}

        return {'status':True,'msj':'Success'}  

    def set_fecha(self,fecha):

        self.fecha = fecha

        return True

    def get(self):
        
        return True
    
    def get_data_reporting_day(self,mode,day):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE samb_entrys.type_account = %s AND DAYOFWEEK(samb_entrys_results.registration_date) = %s AND TIME(samb_entrys_results.registration_date) BETWEEN %s AND %s"

            self.cursor_db.execute(query, (mode, day,int(self.start_date),int(self.end_date)))

            result = self.cursor_db.fetchone() 
            
        except Exception:

            return "NULL"
        
        return result[0]

    def get_data_reporting_curdate(self,mode):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE samb_entrys.type_account = %s AND DATE(samb_entrys_results.registration_date) = CURDATE() AND TIME(samb_entrys_results.registration_date) BETWEEN %s AND %s"

            self.cursor_db.execute(query, (mode,int(self.start_date),int(self.end_date)))

            result = self.cursor_db.fetchone() 
            
        except Exception:

            return "NULL"
        
        return result[0]

    def get_data_reporting_total(self,mode):

        try:

            query = "SELECT IFNULL(SUM(samb_entrys_results.result), 0) as result FROM samb_entrys_results INNER JOIN samb_entrys ON samb_entrys.id = samb_entrys_results.id_entrys_id WHERE samb_entrys.type_account = %s AND TIME(samb_entrys_results.registration_date) BETWEEN %s AND %s"

            self.cursor_db.execute(query, (mode,int(self.start_date),int(self.end_date)))

            result = self.cursor_db.fetchone() 
            
        except Exception:

            return "NULL"
        
        return result[0]

class repositories_smtp(repositories_notifications,irepositories_smtp):

    def __init__(self,cursor):

        super().__init__(cursor)

        self.message = ""

        self.set_message_body()

        self.subject = "Notificaciones de excepciones | SAMB | TRADING "

        self.subject_reports = "Management report ("+config("PROJECT_NAME")+") SESSION NOMINAL | SAMB | TRADING "

        self.destinatario = config("EMAIL_RECIPIENT")

        self.password_email = config("SECRET_EMAIL")

        self.email = config("EMAIL_SEND")

        self.from_email = "Notificaciones  SAMB <"+self.email+">"

        self.server = config("SERVER_SMTP")

        self.port = config("PORT_SMTP")

        self.messsage_report=""

    def set_subject_reports(self,valor):

        self.subject_reports = valor

        return True

    def set_message_report(self,valor):

        self.messsage_report=valor

        return True

    def get_structura_reporte(self,mensaje):

        return """  <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;" align="center" ><b>REPORTES</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: left;"> <table width="60%" align="center" border="1"><thead><tr align="center"><td>DAY</td><td>DEMO</td><td>REAL</td></tr></thead><tbody align="center">"""+mensaje+"""</tbody></table> </td></tr></table> """
        
    def get_encabezado(self): 

        return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />	<title>".$msj_titulo."</title> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> </head> <body style="margin: 0; padding: 0;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="padding: 10px 0 30px 0;"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc; border-collapse: collapse;">	<tr> <td align="center" bgcolor="#ffffff" style="padding: 5px 5px 5px 5px;"> """
    
    def get_pie(self):

        return """</td> </tr> <tr> <td bgcolor="#340049" style="padding: 30px 30px 30px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="100%"><font color="#ffffff"></font><i>Esta es una cuenta de correo solo informativa, por favor no responder este correo.</i></td> </tr> </table>	</td> </tr>	</table> </td> </tr> </table> </body> </html>"""

    def set_message(self,mensaje):

        self.message = mensaje

        return True

    def set_message_body(self):

        self.cuerpo = """ <tr> <td bgcolor="#ffffff" style="padding: 20px 30px 5px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;"><b>EXCEPCIONES</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: justify;">"""+self.message+"""</td> </tr> <tr> <td> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td width="260" valign="top"> </td> <td style="font-size: 4; line-height: 0;" width="20"> &nbsp; </td> <td width="260" valign="top"> </td> </tr> </table> </td> </tr> </table> </td> </tr>  """
        
        return True
        
    def send(self,fecha,mensaje):

        self.set_fecha(fecha)

        self.set_message(mensaje)

        self.add_notificacion_exc(mensaje)

        try:
        
            _msg = email.message.Message()

            _msg["Subject"] = self.subject

            _msg["From"] = self.from_email

            _msg["To"] = self.destinatario

            _password = self.password_email

            _correo = self.email
            
            _msg.add_header("Content-Type", "text/html")
            
            _msg.set_payload(self.set_message_body())
            
            _s = smtplib.SMTP(self.server+": "+self.port)
            
            _s.starttls()
            
            # Login Credentials for sending the mail
            _s.login(_correo, _password)
            
            _s.sendmail(_msg["From"], [_msg["To"]], _msg.as_string())

            _s.quit()

        except Exception as err:

            return {"status": False, "message":"Hubo una incidencia en el envio del mensaje SMTP: "+str(err)}
        
        return True
    
    def send_reports(self,fecha,mensaje):

        self.set_fecha(fecha)

        self.set_message_report(self.get_structura_reporte(mensaje))

        self.add_reports()

        try:
        
            _msg = email.message.Message()

            _msg["Subject"] = self.subject_reports

            _msg["From"] = self.from_email

            _msg["To"] = self.destinatario

            _password = self.password_email

            _correo = self.email
            
            _msg.add_header("Content-Type", "text/html")

            _msg.set_payload(self.messsage_report)
            
            _s = smtplib.SMTP(self.server+": "+self.port)
            
            _s.starttls()
            
            # Login Credentials for sending the mail
            _s.login(_correo, _password)
            
            _s.sendmail(_msg["From"], [_msg["To"]], _msg.as_string())

            _s.quit()

        except Exception as err:

            return {"status": False, "message":"Hubo una incidencia en el envio del mensaje SMTP: "+str(err)}
        
        return True

    def get_data_reporting(self,mode,day):

        return self.get_data_reporting_day(mode,day)
    
    def get_data_reporting_cur(self,mode):

        return self.get_data_reporting_curdate(mode)
    
    def get_data_reporting_tot(self, mode):

        return self.get_data_reporting_total(mode)

class repositories_telegram(repositories_notifications,irepositories_telegram):

    def __init__(self,cursor):

        self.base_url = config("URL_TELEGRAM")

        self.chat_id = config("CHAT_ID")

        super().__init__(cursor)

    def send(self, mensaje):

        try:

            url = self.base_url
            
            params = {
            
                'chat_id': self.chat_id,
            
                'text': mensaje
            
            }
            
            response = requests.post(url, params=params)

            if response.status_code != 200:

                return {'status':False,'message':'Error al enviar el mensaje. Codigo de respuesta:'+str(response.status_code)}

        except Exception as err:

            return {'status': False, 'message':'Hubo una incidencia en el envio del mensaje por telegram: '+str(err)}
        
        return {'status': True, 'message':'Success'}
    
    def add(self,mensaje,response,id_cronjobs,fecha):

        self.set_fecha(fecha)

        return self.add_notification_telegram(mensaje,response,id_cronjobs)
            