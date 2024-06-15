from unittest import TestCase, mock

from unittest.mock import patch

from apis.services.iq import cases_iq

from apis.services.smtp import cases_smtp

from decimal import Decimal

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

    @mock.patch('apis.services.iq.IQ_Option')
    def test_init_success(self, mock_get):

        mock_instance = mock_get.return_value

        mock_instance.connect.return_value = True

        mock_instance.check.return_value = {'status':True,'msj':'Success sync'}

        result = self.service.init()

        self.assertEqual(result, {'status':True,'msj':'Success sync'})
  
    @mock.patch('apis.services.iq.IQ_Option')
    def test_check_success(self, mock_iq_option):

        expected_result = {'status': True, 'msj': 'Success sync'}

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.check_connect.return_value = True

        self.service.init()

        result = self.service.check()
        
        self.assertEqual(result, expected_result)

    @mock.patch('apis.services.iq.IQ_Option')
    def test_set_balance(self, mock_iq_option):

        expected_result = {'status':True,'msj':'Success'}

        mock_instance = mock_iq_option.return_value

        mock_instance.connect.return_value = True

        mock_instance.check_connect.return_value = True

        self.service.init()

        result = self.service.set_balance()
        
        self.assertEqual(result, expected_result)

    @mock.patch('apis.services.iq.IQ_Option')
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

    @mock.patch.object(cases_iq, 'removed_candle_close', return_value=[Decimal("1.04"), Decimal("1.05"), Decimal("1.06")])
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
        
        self.assertEqual(result, "LONG")


    @mock.patch('apis.services.iq.cases_iq.iq')
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