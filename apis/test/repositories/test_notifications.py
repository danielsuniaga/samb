from unittest import TestCase, mock

from apis.repositories.notification import repositories_notifications,repositories_smtp,repositories_telegram

class TestRepositoriesNotifications(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_notifications(self.mock_cursor)

        self.new_date = "2024-06-01"

    def test_add_entrys_success(self):

        result = self.repo.add_notificacion_exc('TEST')

        self.assertTrue(result)

    def test_add_reports_success(self):

        result = self.repo.add_reports()

        self.assertTrue(result)

    def test_removed_special_characters(self):

        test_cases = [
            ("hello", "hello"),  # Sin caracteres especiales
            ("it's", "its"),  # Eliminar comilla simple
            ("", ""),  # Cadena vacía
            ("   ", "   ")  # Espacios en blanco
        ]

        for value, expected_result in test_cases:

            with self.subTest(value=value):

                result = self.repo.removed_special_characters(value)

                self.assertEqual(result, expected_result)

    def test_add_notification_telegram_success(self):

        result = self.repo.add_notification_telegram('TEST','TEST','TEST')

        self.assertTrue(result)

    def test_set_fecha(self):

        date = self.new_date

        result = self.repo.set_fecha(date)
        
        self.assertEqual(self.repo.fecha, date)
        
        self.assertTrue(result)

    def test_get(self):

        result = self.repo.get()
        
        self.assertTrue(result)

    def test_get_data_reporting_day(self):

        mode = "some_mode"

        day = 1

        self.mock_cursor.fetchone.return_value = (10,) 

        result = self.repo.get_data_reporting_day(mode, day)

        self.assertEqual(result, 10)

    def test_get_data_reporting_curdate(self):

        mode = "some_mode"

        self.mock_cursor.fetchone.return_value = (10,) 

        result = self.repo.get_data_reporting_curdate(mode)

        self.assertEqual(result, 10)

    def test_get_data_reporting_total(self):

        mode = "some_mode"

        self.mock_cursor.fetchone.return_value = (10,) 

        result = self.repo.get_data_reporting_total(mode)

        self.assertEqual(result, 10)

class TestRepositoriesSMTP(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_smtp(self.mock_cursor)

        self.new_value = "new_value"

        self.mode = "some_mode"

        self.new_date = "2024-06-01"

        self.expected_result = "expected_result"

    def test_set_message_report(self):

        value = self.new_value

        result = self.repo.set_message_report(value)
        
        self.assertEqual(self.repo.messsage_report, value)
        
        self.assertTrue(result)

    def test_get_structura_reporte(self):

        mensaje = "<tr><td>Lunes</td><td>100</td><td>200</td></tr>"
        
        result = self.repo.get_structura_reporte(mensaje)

        expected_result = """  <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;" align="center" ><b>REPORTES</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: left;"> <table width="60%" align="center" border="1"><thead><tr align="center"><td>DAY</td><td>DEMO</td><td>REAL</td></tr></thead><tbody align="center"><tr><td>Lunes</td><td>100</td><td>200</td></tr></tbody></table> </td></tr></table> """
        
        self.assertEqual(result, expected_result)

    def test_get_encabezado(self):
        
        result = self.repo.get_encabezado()

        expected_result = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />	<title>".$msj_titulo."</title> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> </head> <body style="margin: 0; padding: 0;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="padding: 10px 0 30px 0;"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc; border-collapse: collapse;">	<tr> <td align="center" bgcolor="#ffffff" style="padding: 5px 5px 5px 5px;"> """
        
        self.assertEqual(result, expected_result)

    def test_get_pie(self):
        
        result = self.repo.get_pie()

        expected_result = """</td> </tr> <tr> <td bgcolor="#340049" style="padding: 30px 30px 30px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="100%"><font color="#ffffff"></font><i>Esta es una cuenta de correo solo informativa, por favor no responder este correo.</i></td> </tr> </table>	</td> </tr>	</table> </td> </tr> </table> </body> </html>"""
        
        self.assertEqual(result, expected_result)

    def test_set_message(self):

        message = self.new_value

        result = self.repo.set_message(message)
        
        self.assertEqual(self.repo.message, message)
        
        self.assertTrue(result)

    def test_message_body(self):

        result = self.repo.set_message_body()

        self.assertTrue(result)

        expected_cuerpo = """ <tr> <td bgcolor="#ffffff" style="padding: 20px 30px 5px 30px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td style="color: #340049; font-family: Arial, sans-serif; font-size: 24px;"><b>EXCEPCIONES</b></td> </tr> <tr> <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;text-align: justify;">""" + self.repo.message + """</td> </tr> <tr> <td> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td width="260" valign="top"> </td> <td style="font-size: 4; line-height: 0;" width="20"> &nbsp; </td> <td width="260" valign="top"> </td> </tr> </table> </td> </tr> </table> </td> </tr>  """
        
        self.assertEqual(self.repo.cuerpo, expected_cuerpo)

    def test_send(self): 

        message_email = self.new_value

        date = self.new_date

        result = self.repo.send(date,message_email)

        self.assertTrue(result)

    def test_get_data_reporting(self):

        mode = self.mode

        day = 1

        self.repo.get_data_reporting_day = mock.MagicMock(return_value=42)

        result = self.repo.get_data_reporting(mode, day)

        self.assertEqual(result, 42)

    def test_get_data_reporting_cur(self):

        mode = self.mode

        self.repo.get_data_reporting_curdate = mock.MagicMock(return_value=42)

        result = self.repo.get_data_reporting_cur(mode)

        self.assertEqual(result, 42)

    def test_get_data_reporting_tot(self):

        mode = self.mode

        self.repo.get_data_reporting_total = mock.MagicMock(return_value=42)

        result = self.repo.get_data_reporting_tot(mode)

        self.assertEqual(result, 42)

class TestRepositoriesTelegram(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.repo = repositories_telegram(self.mock_cursor)

        self.new_date = "2024-06-01"

        self.expected_result = "expected_result"

    def test_send(self):

        mensaje = "some_message"

        result = self.repo.send(mensaje)

        self.assertEqual(result, {'status': True, 'message':'Success'})

    def test_add(self):

        mensaje = "TEST"

        response = "TEST"

        id_cronjobs = 123

        fecha = self.new_date

        self.repo.set_fecha = mock.MagicMock()

        self.repo.add_notification_telegram = mock.MagicMock(return_value=self.expected_result)

        result = self.repo.add(mensaje, response, id_cronjobs, fecha)

        self.assertEqual(result, self.expected_result)