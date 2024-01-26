from email import message

import smtplib

import email.message

import uuid

class class_notifications():

    fecha = ""

    cursor_db = ""

    id_exceptions_api = '2be31b6ea99b4e3aa2011a95e45af005'

    def __init__(self,fecha,cursor):

        self.fecha = fecha

        self.cursor_db = cursor

    def get(self):

        return True

    def write_notificacion_exc(self,mensaje):

        try:

            _fecha_actual = self.fecha.strftime("%Y%m%d%H%M%S")

            self.cursor_db.execute("INSERT INTO samb_notifications_exceptions_apis_independient(samb_notifications_exceptions_apis_independient.id,samb_notifications_exceptions_apis_independient.description, samb_notifications_exceptions_apis_independient.registration_date,samb_notifications_exceptions_apis_independient.update_date,samb_notifications_exceptions_apis_independient.condition, samb_notifications_exceptions_apis_independient.id_exceptions_api_id)VALUES(%s,%s,%s,%s,%s,%s)",[uuid.uuid4().hex, mensaje, _fecha_actual, _fecha_actual, "1", self.id_exceptions_api])

        except Exception as err:

            return False

        return True       

class class_smtp(class_notifications):

    encabezado = ''

    cuerpo = ''

    pie = ''

    message = ''

    subject = ''

    from_email = ''

    destinatario = ''

    password_email = ''

    email = ''

    def __init__(self,fecha,cursor): 

        super().__init__(fecha,cursor)

        self.set_message_body()

        self.subject = "Notificaciones de excepciones | SAMB | TRADING "

        self.from_email = "Notificaciones  SAMB <notificacionesinternas@guardcontrol.co>"

        self.destinatario = "danieldsuniaga@gmail.com"

        self.password_email = "samb$2024."

        self.email = "notificacionesinternas@guardcontrol.co"

    def set_message_body(self):

        self.encabezado="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />	<title>".$msj_titulo."</title> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> </head> <body style="margin: 0; padding: 0;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="padding: 10px 0 30px 0;"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc; border-collapse: collapse;">	<tr> <td align="center" bgcolor="#ffffff" style="padding: 5px 5px 5px 5px;"> """

        self.cuerpo = """ <tr> <td bgcolor="#ffffff" style="padding: 20px 30px 5px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;"><b>EXCEPCIONES</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: justify;">"""+self.message+"""</td> </tr> <tr> <td> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td width="260" valign="top"> </td> <td style="font-size: 4; line-height: 0;" width="20"> &nbsp; </td> <td width="260" valign="top"> </td> </tr> </table> </td> </tr> </table> </td> </tr>  """

        self.pie= """</td> </tr> <tr> <td bgcolor="#340049" style="padding: 30px 30px 30px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="100%"><font color="#ffffff"></font><i>Esta es una cuenta de correo solo informativa, por favor no responder este correo.</i></td> </tr> </table>	</td> </tr>	</table> </td> </tr> </table> </body> </html>"""

        return self.encabezado+self.cuerpo+self.pie

    def send(self,mensaje):

        self.write_notificacion_exc(mensaje)

        self.message = mensaje
    
        try:
        
            _msg = email.message.Message()

            _msg["Subject"] = self.subject

            _msg["From"] = self.from_email

            _msg["To"] = self.destinatario

            _password = self.password_email

            _correo = self.email
            
            _msg.add_header("Content-Type", "text/html")
            
            _msg.set_payload(self.set_message_body())
            
            _s = smtplib.SMTP("mail.guardcontrol.co: 26")
            
            _s.starttls()
            
            # Login Credentials for sending the mail
            _s.login(_correo, _password)
            
            _s.sendmail(_msg["From"], [_msg["To"]], _msg.as_string())

            _s.quit()

        except Exception as err:

            return {"status": True, "message":"Hubo una incidencia en el envio del mensaje SMTP: "+str(err)}
        
        return True
    

