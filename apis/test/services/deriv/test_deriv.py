from unittest import TestCase, mock

from unittest.mock import patch

import unittest

import apis.services.deriv.de_core as de_core

import asyncio
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
        # Inicializar conexión
        result = await self.services.init_deriv()
        print("Apertura: ", result)

        # Verificar si la conexión fue exitosa
        if not result['status']:
            print("Error al inicializar la conexión.")
            return

        # Parámetros del contrato
        symbol = 'R_100'
        amount = 1
        contract_type = "CALL"
        duration = 1  # 1 minuto
        duration_unit = "m"

        # Generar propuesta
        symbols_result = await self.services.generate_proposal(symbol, amount, contract_type, duration, duration_unit)
        if symbols_result.get('proposal_id') is None:
            print("Error al generar propuesta: proposal_id es None.")
            await self.services.close_deriv()
            return
        print("Propuesta generada: ", symbols_result)

        # Ejecutar propuesta
        execute = await self.services.execute_proposal(symbols_result['proposal_id'])
        if not execute['status']:
            print("Error al ejecutar la propuesta: ", execute)
            await self.services.close_deriv()
            return
        print("Propuesta ejecutada: ", execute)

        # Obtener el contract_id
        contract_id = execute['execution_details']['buy'].get('contract_id')
        if not contract_id:
            print("Error: No se pudo obtener el contract_id.")
            await self.services.close_deriv()
            return
        print(f"Contrato ejecutado con éxito. ID: {contract_id}")

        # Esperar el tiempo necesario para verificar el resultado
        print(f"Esperando {duration} {duration_unit} para verificar el resultado...")

        duration_total = (duration * 60) + 5
        await asyncio.sleep(duration_total)

        # Verificar resultado del contrato
        contract_result = await self.services.check_position_result(contract_id)
        if not contract_result:
            print("Error al obtener el resultado del contrato.")
        else:
            print("Resultado del contrato: ", contract_result)

        # Cerrar conexión
        result_close = await self.services.close_deriv()
        print("Closed: ", result_close)

    async def test_check_position_result(self):

        contract_id = 267591023888

        result = await self.services.init_deriv()
        print("Apertura: ", result)

        if not result['status']:
            print("Error al inicializar la conexión.")
            return
        
        contract_result = await self.services.check_position_result(contract_id)
        if not contract_result:
            print("Error al obtener el resultado del contrato.")
        else:
            print("Resultado del contrato: ", contract_result)


        result_close = await self.services.close_deriv()
        print("Closed: ", result_close)






