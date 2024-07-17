from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.iq.iq import cases_iq

from apis.services.smtp.smtp import cases_smtp

from decimal import Decimal

import apis.services.dates.dates as case_dates

import apis.services.telegram.telegram as case_telegram

from django.db import connection

class TestServicesIq(TestCase):

    def setUp(self):

        self.mock_cursor = mock.MagicMock()
        
        self.service = cases_iq(self.mock_cursor)

        self.expected_message_general = "TEST"

    def test_set_message(self):

        result = self.service.set_message("TEST")
        
        self.assertTrue(result)
    
    def test_add_message_text(self):

        expected_message = "Initial Message - New Value"

        self.service.message = "Initial Message"

        result = self.service.add_message_text("New Value")

        self.assertTrue(result)

        self.assertEqual(self.service.message, expected_message)

    def test_set_value_rsi(self):

        expected_message = "TEST"

        self.service.rsi = expected_message

        result = self.service.set_value_rsi(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.rsi, expected_message)

    def test_set_value_sma10(self):

        expected_message = self.expected_message_general

        self.service.sma10 = expected_message

        result = self.service.set_value_sma10(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.sma10, expected_message)

    def test_set_value_sma30(self):

        expected_message = self.expected_message_general

        self.service.sma30 = expected_message

        result = self.service.set_value_sma30(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.sma30, expected_message)

    def test_generate_id(self):

        cronjob_id = self.service.generate_id()

        self.assertIsInstance(cronjob_id, str)

        unique_ids = set()

        unique_ids.add(cronjob_id)

        for _ in range(1000):  

            new_id = self.service.generate_id()

            self.assertNotIn(new_id, unique_ids)

            unique_ids.add(new_id)

    def test_set_type(self):

        expected_message = self.expected_message_general

        self.service.type = expected_message

        result = self.service.set_type(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.type, expected_message)

    def test_set_current_date(self):

        expected_message = self.expected_message_general

        self.service.current_date = expected_message

        result = self.service.set_current_date(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.current_date, expected_message)

    def test_set_current_date_general(self):

        expected_message = self.expected_message_general

        self.service.current_date_general = expected_message

        result = self.service.set_current_date_general(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.current_date_general, expected_message)

    def test_set_current_date_manipulated(self):

        expected_message = self.expected_message_general

        self.service.current_date_manipulated = expected_message

        result = self.service.set_current_date_manipulated(expected_message)

        self.assertTrue(result)

        self.assertEqual(self.service.current_date_manipulated, expected_message)

    @mock.patch('apis.services.iq.iq_core.IQ_Option')
    def test_init_success(self, mock_get):

        mock_instance = mock_get.return_value

        mock_instance.connect.return_value = True

        mock_instance.check.return_value = {'status':True,'msj':'Success sync'}

        result = self.service.init()

        self.assertEqual(result, {'status':True,'msj':'Success sync'})
  
    @mock.patch('apis.services.iq.iq_core.IQ_Option')
    def test_check_success(self, mock_iq_option):

        expected_result = {'status': True, 'msj': 'Success sync'}

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.check_connect.return_value = True

        self.service.init()

        result = self.service.check()
        
        self.assertEqual(result, expected_result)

    @mock.patch('apis.services.iq.iq_core.IQ_Option')
    def test_set_balance(self, mock_iq_option):

        date = case_dates.cases_dates()

        expected_result = {'status':True,'msj':'Success'}

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.check_connect.return_value = True

        self.service.init()

        result = self.service.set_balance(date)
        
        self.assertEqual(result, expected_result)

    @mock.patch('apis.services.iq.iq_core.IQ_Option')
    def test_get_candles_data(self, mock_iq_option):

        expected_result = [
            {"from": 1623693067, "close": 1.23456},
            {"from": 1623693068, "close": 1.23457},
            {"from": 1623693069, "close": 1.23458}
        ]

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.get_candles.return_value = expected_result

        self.service.init()

        result = self.service.get_candles_data()
        
        self.assertEqual(result, expected_result)

    def test_removed_candle_last(self):

        candles = [
            {"from": 1623693067, "close": 1.23456},
            {"from": 1623693068, "close": 1.23457},
            {"from": 1623693069, "close": 1.23458}
        ]

        expected_result = [
            {"from": 1623693067, "close": 1.23456},
            {"from": 1623693068, "close": 1.23457}
        ]

        result = self.service.removed_candle_last(candles)

        self.assertEqual(result, expected_result)

    def test_removed_candle_close(self):

        candles = [
            {"from": 1623693067, "close": "1.23456"},
            {"from": 1623693068, "close": "1.23457"},
            {"from": 1623693069, "close": "1.23458"}
        ]

        amount = 2

        expected_result = [Decimal('1.23457')]

        result = self.service.removed_candle_close(candles, amount)

        # print(result)

        self.assertEqual(result, expected_result)

    @mock.patch.object(cases_iq, 'removed_candle_close', return_value=[Decimal("1.03"),Decimal("1.04"), Decimal("1.05"), Decimal("1.06")])
    def test_analized_candles_long(self,mock_get):

        candles = [
            {"close": Decimal("1.06")},
            {"close": Decimal("1.05")},
            {"close": Decimal("1.04")},
            {"close": Decimal("1.03")},
            {"close": Decimal("1.02")}
        ]
   
        self.service.candle_removed = 1
        self.service.candle_analized = 3
        self.service.type_entry_long = "LONG"
        self.service.type_entry_short = "SHORT"
        self.service.project_name = "Test Project"
        self.service.mode = "Test Mode"
        self.service.par = "EURUSD"
        self.service.message_entry_long = "Entry Long Message"
        self.service.message_entry_short = "Entry Short Message"
        
        result = self.service.analized_candles(candles)
        
        self.assertEqual(result, "SHORT")

    @mock.patch('apis.services.iq.iq.cases_iq.iq')
    def test_get_current_entrys_success(self,mock_iq):

        flash = "call"

        smtp = "TEST"

        mock_iq_instance = mock_iq.return_value

        mock_iq_instance.get_current_entrys.return_value = {'status': True, 'msj': 'Success'}

        mock_iq_instance.get_current_entrys_min.return_value = {'status': True, 'msj': 'Success'}

        self.service.iq = mock_iq_instance

        result = self.service.get_current_entrys(flash, smtp)

        self.assertTrue(result)

    def test_get_rsi_mixed_changes(self):

        candles = [Decimal("1.0"), Decimal("1.2"), Decimal("1.1"), Decimal("1.3"), Decimal("1.2")]

        periodos = 4

        result = self.service.get_rsi(candles, periodos)

        self.assertTrue(0 <= result <= 100)  

    @mock.patch.object(cases_iq, 'get_rsi', return_value=Decimal("50"))
    @mock.patch.object(cases_iq, 'removed_candle_close', return_value=[Decimal("1.05"), Decimal("1.04"), Decimal("1.03"), Decimal("1.02")])
    def test_analized_rsi_in_range(self, mock_get_rsi, mock_get):
        
        candles = [
            {"close": Decimal("1.06")},
            {"close": Decimal("1.05")},
            {"close": Decimal("1.04")},
            {"close": Decimal("1.03")},
            {"close": Decimal("1.02")}
        ]

        result = self.service.analized_rsi(candles)

        self.assertTrue(result)

    @mock.patch.object(cases_iq, 'removed_candle_close', return_value=[Decimal("1.06"), Decimal("1.05"), Decimal("1.04"), Decimal("1.03"), Decimal("1.02")])
    def test_get_sma(self, mock_removed_candle_close):

        candles = [
            {"close": Decimal("1.06")},
            {"close": Decimal("1.05")},
            {"close": Decimal("1.04")},
            {"close": Decimal("1.03")},
            {"close": Decimal("1.02")}
        ]
        
        account_candles = 5
        
        type_sma = 3

        expected_sma = (Decimal("1.04") + Decimal("1.03") + Decimal("1.02")) / Decimal(type_sma)

        result = self.service.get_sma(candles, type_sma, account_candles)

        self.assertEqual(result, expected_sma)

    @mock.patch.object(cases_iq, 'removed_candle_close', return_value=[Decimal("1.06"), Decimal("1.05"), Decimal("1.04"), Decimal("1.03"), Decimal("1.02")])
    @mock.patch.object(cases_iq, 'get_sma', return_value=Decimal("1.04"))
    @mock.patch.object(cases_iq, 'set_value_sma10', return_value=True)
    @mock.patch.object(cases_iq, 'set_value_sma30', return_value=True)
    def test_analized_sma_short(self,mock_set_value_sma30, mock_set_value_sma10, mock_get_sma, mock_removed_candle_close):

        candles = [
            {"close": Decimal("1.06")},
            {"close": Decimal("1.05")},
            {"close": Decimal("1.04")},
            {"close": Decimal("1.03")},
            {"close": Decimal("1.02")}
        ]

        self.service.type = "put"

        self.service.sma_short = 10

        self.service.candle_sma_short = 10

        self.service.sma_long = 30

        self.service.candle_sma_long = 30

        self.service.candle_last = 5

        self.service.last = 0 

        self.service.type_entry_short = "call"

        self.service.type_entry_long = "put"

        result = self.service.analized_sma(candles)

        self.assertTrue(result)

    @mock.patch.object(cases_iq, 'analized_rsi', return_value=True)
    @mock.patch.object(cases_iq, 'analized_sma', return_value=True)
    def test_get_indicators_both_active_true(self,mock_rsi,mock_sma):

        candles = [
            {"close": Decimal("1.06")},
            {"close": Decimal("1.05")},
            {"close": Decimal("1.04")},
            {"close": Decimal("1.03")},
            {"close": Decimal("1.02")}
        ]

        self.service.active_rsi = True

        self.service.active_sma = True

        result = self.service.get_indicators(True, candles)

        self.assertTrue(result)
    
    @mock.patch.object(cases_iq, 'add_result_entry_platform_v3', return_value=2)
    @mock.patch('apis.repositories.iq.iq.repositories_iq.add_entrys', return_value={'status': True, 'msj': 'Success'})
    @mock.patch.object(cases_iq, 'add_indicators', return_value=True)
    def test_add_entry_traceability(self,mock_add_indicators,mock_add_entrys,mock_add_result_entry_platform_v3):

        result = True

        id_cronjobs = "Test"

        self.service.current_date_general = '2024-06-14'

        self.service.type = 'test_type'

        self.service.message = ""

        result_candles = 'test_result_candles'

        smtp = mock.Mock()

        result_value = self.service.add_entry_traceability(result, id_cronjobs, smtp, result_candles)

        self.assertTrue(result_value)

    @mock.patch('apis.repositories.iq.iq.repositories_iq.add_indicators', return_value={'status': True, 'msj': 'Success'})
    @mock.patch.object(cases_iq, 'add_movements', return_value=True)
    def test_add_indicators_success(self,mock_add_indicators,mock_add_movements):

        smtp = mock.Mock()

        result_candles = 'test_result_candles'

        self.service.current_date_general = '2024-06-14'

        result_value = self.service.add_indicators(smtp, result_candles)

        self.assertTrue(result_value)

    @mock.patch('apis.repositories.iq.iq.repositories_iq.add_movements', return_value={'status': True, 'msj': 'Success'})
    @mock.patch.object(cases_iq, 'add_result_entry', return_value=True)
    @mock.patch('apis.repositories.iq.iq.repositories_iq.get_id_entry', return_value='entry_id')
    def test_add_movements_success(self,mock_add_movements,mock_add_result_entry, mock_get_id_entry):

        smtp = mock.Mock()

        result_candles = [
            {"at": '2024-06-14T00:00:00Z', "close": Decimal("1.06"), "from": 'source1', "id": 'candle1', "max": Decimal("1.10"), "min": Decimal("1.00"), "open": Decimal("1.05"), "to": 'destination1', "volume": Decimal("100")},
            {"at": '2024-06-14T01:00:00Z', "close": Decimal("1.05"), "from": 'source2', "id": 'candle2', "max": Decimal("1.09"), "min": Decimal("1.01"), "open": Decimal("1.04"), "to": 'destination2', "volume": Decimal("150")},
            {"at": '2024-06-14T02:00:00Z', "close": Decimal("1.04"), "from": 'source3', "id": 'candle3', "max": Decimal("1.08"), "min": Decimal("1.02"), "open": Decimal("1.03"), "to": 'destination3', "volume": Decimal("200")}
        ]

        self.service.current_date_general = '2024-06-14'

        result_value = self.service.add_movements(smtp, result_candles)

        self.assertTrue(result_value)

    @mock.patch('apis.repositories.iq.iq.repositories_iq.add_entrys_result', return_value={'status': True, 'msj': 'Success'})
    def test_add_result_entry_success(self,mock_add_entrys_result):

        smtp = mock.Mock()

        self.service.current_date_general = '2024-06-14'

        result_value = self.service.add_result_entry(smtp)

        self.assertTrue(result_value)

    @mock.patch('apis.services.telegram.telegram.cases_telegram.send', return_value=True)
    def test_send_notification_telegram_success(self, mock_telegram_send):

        result = True

        id_cronjobs = "Test"

        result_value = self.service.send_notification_telegram(result, mock_telegram_send, id_cronjobs)

        self.assertTrue(result_value)

    @mock.patch('apis.services.iq.iq_core.IQ_Option')
    def test_add_result_entry_platform_v3_success(self, mock_iq_option):

        result=1234456577

        expected_result = 1

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.check_win_v3.return_value = expected_result

        self.service.init()

        result = self.service.add_result_entry_platform_v3(result)

        self.assertEqual(result,expected_result)

    @mock.patch('apis.repositories.iq.iq.repositories_iq.get_sum_entrys_date', return_value={'status':True,'data': 1,'msj':'Success'})
    def test_get_monetary_filter(self,mock_get_sum_entrys_date):

        result = True

        smtp = True

        self.service.profit=2

        self.service.loss=-4

        result = self.service.get_monetary_filter(result,smtp)

        self.assertTrue(result)

    def test_get_par(self):

        expected_result = "TEST"

        self.service.par = expected_result

        result = self.service.get_par()

        self.assertEqual(expected_result,result)

    def test_set_par(self):

        valor = "TEST"

        result = self.service.set_par(valor)

        self.assertTrue(result)

    @mock.patch('apis.services.dates.dates.cases_dates.get_day', return_value=6)
    def test_analized_day_true(self,mock_date):

        date = case_dates.cases_dates()
        
        result = self.service.analized_day(date)

        self.assertTrue(result)

    @mock.patch.object(cases_iq, 'analized_day', return_value=True)
    def test_set_asset_financial(self,mock_analized_day):

        date = case_dates.cases_dates()

        result = self.service.set_asset_financial(date)

        self.assertTrue(result)

    @mock.patch('apis.repositories.iq.iq.repositories_iq.get_type_manager_day', return_value={'status':True,'data': 1,'msj':'Success'})
    def test_get_type_manager_day(self,mock_iq_get_type_manager_day):

        expected_result = 1

        day=3

        result = self.service.get_type_manager_day(day)

        self.assertEqual(result,expected_result)

    def test_set_mode(self):

        valor="TEST"

        result = self.service.set_mode(valor)

        self.assertTrue(result)

    def test_get_mode(self):

        expected_result = "REAL"

        self.service.mode = expected_result

        result = self.service.get_mode()

        self.assertEqual(expected_result,result)

    @mock.patch.object(cases_iq, 'get_type_manager_day', return_value=1)
    def test_analized_mode(self,mock_get_type_manager_day):
        

        date = case_dates.cases_dates()

        result = self.service.analized_mode(date)

        self.assertTrue(result)

    @mock.patch.object(cases_iq, 'set_asset_financial', return_value=True)
    @mock.patch.object(cases_iq, 'analized_mode', return_value=True)
    @mock.patch.object(cases_iq, 'set_current_date', return_value=True)
    @mock.patch.object(cases_iq, 'set_current_date_general', return_value=True)
    @mock.patch.object(cases_iq, 'set_current_date_manipulated', return_value=True)
    @mock.patch.object(cases_iq, 'get_current_entrys', return_value=True)
    @mock.patch.object(cases_iq, 'get_indicators', return_value=True)
    @mock.patch.object(cases_iq, 'get_monetary_filter', return_value=True)
    @mock.patch.object(cases_iq, 'add_entry_platform', return_value=True)
    @mock.patch.object(cases_iq, 'add_entry_traceability', return_value=True)
    @mock.patch.object(cases_iq, 'send_notification_telegram', return_value=True)
    def test_get_loops(self,mock_set_asset_financial,mock_analized_mode,mock_set_current_date,mock_set_current_date_general,mock_set_current_date_manipulated,mock_get_current_entrys,mock_get_indicators,mock_get_monetary_filter,mock_add_entry_platform,mock_add_entry_traceability,mock_send_notification_telegram):

        cursor = connection.cursor()

        date = case_dates.cases_dates()

        telegram = case_telegram.cases_telegram(cursor)

        smtp = "test"

        id_cronjobs = "11111111111"

        self.service.sleep = 0

        self.service.number_loops = 1

        self.service.init()

        result = self.service.get_loops(date,smtp,id_cronjobs,telegram)

        self.assertTrue(result)

