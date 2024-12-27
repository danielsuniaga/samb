from unittest import TestCase, mock

from unittest.mock import patch

import unittest

import apis.services.deriv.de_core as de_core

class TestServicesDeriv(unittest.IsolatedAsyncioTestCase):

    services = None

    def setUp(self):

        self.services = de_core.de_core()

    async def test_init_deriv(self):

        result = await self.services.init_deriv()

        print("Apertura: ",result)

        result = await self.services.get_balance()

        print("Balance: ",result)

        result = await self.services.get_candles(symbol='frxEURUSD')

        print("Result asset: ",result)

        result_close = await self.services.close_deriv()

        print("Closed: ",result_close)

    async def test_get_balance(self):

        result = await self.services.init_deriv()

        print("Apertura: ", result)

        if result['status']:

            symbols_result = await self.services.get_balance()

            print("Balance: ", symbols_result)

        result_close = await self.services.close_deriv()

        print("Closed: ", result_close)

    async def test_get_candles(self):

        result = await self.services.init_deriv()

        print("Apertura: ", result)

        if result['status']:

            symbols_result = await self.services.get_candles('frxEURUSD')

            print("Status asset: ", symbols_result)

        result_close = await self.services.close_deriv()

        print("Closed: ", result_close)

    async def test_get_active_symbols(self):

        result = await self.services.init_deriv()

        print("Apertura: ", result)

        if result['status']:

            symbols_result = await self.services.get_active_symbols()

            print("Status asset: ", symbols_result)

        result_close = await self.services.close_deriv()

        print("Closed: ", result_close)

    async def test_generate_proposal(self):

        result = await self.services.init_deriv()

        print("Apertura: ", result)

        if result['status']:

            symbol='frxEURUSD'

            amount = 1

            contract_type = "CALL"

            duration = 15

            duration_unit="m"

            symbols_result = await self.services.generate_proposal(symbol, amount, contract_type, duration, duration_unit)

            print("Status proposal: ", symbols_result)

        result_close = await self.services.close_deriv()

        print("Closed: ", result_close)

    async def test_execute_proposal(self):

        result = await self.services.init_deriv()

        print("Apertura: ", result)

        if result['status']:

            symbol='frxEURUSD'

            amount = 1

            contract_type = "CALL"

            duration = 15

            duration_unit="m"

            symbols_result = await self.services.generate_proposal(symbol, amount, contract_type, duration, duration_unit)

            print("Status proposal: ", symbols_result['proposal_id'])

            if symbols_result['proposal_id'] is not None:

                execute = await self.services.execute_proposal(symbols_result['proposal_id'])
                
                print("Status execute:", execute)

            else:
                
                print("Error: proposal_id es None.")

        result_close = await self.services.close_deriv()

        print("Closed: ", result_close)





