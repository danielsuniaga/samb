from decouple import config

from deriv_api import DerivAPI

class de_core():

    token = None

    api = None

    id_app = None

    proposal_env = None

    def __init__(self):

        self.init_token()

        self.init_id_app()

        self.init_proposal_env()

    def init_proposal_env(self):

        self.proposal_env = {
            'basis':config("PROPOSAL_BASIS"),
            'currency':config("PROPOSAL_CURRENCY")
        }

        return True
    
    def get_proposal_env_basis(self):

        return self.proposal_env['basis']
    
    def get_proposal_env_currency(self):

        return self.proposal_env['currency']
        
    def init_token(self):

        self.tokens = {
            'demo': config("TOKEN_DERIV_DEMO"),
            'real': config("TOKEN_DERIV_REAL")
        }

        return True
    
    def init_id_app(self):

        self.id_app = int(config("ID_APP"))

        return True
    
    def get_token_real(self):

        return self.tokens['real']
    
    def get_token_demo(self):

        return self.tokens['demo']
    
    def get_id_app(self):

        return self.id_app
    
    async def check_deriv(self):

        token = self.get_token_demo()

        try:

            response = await self.api.authorize(token)
            
        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al chequear sincronizcion con deriv: '+str(err)}
        
        return {'status': True, 'message':'Conexion exitosa con deriv'}
                
    async def init_deriv(self):

        app_id = self.get_id_app()

        try:

            self.api = DerivAPI(app_id=app_id)
        
        except Exception as err:

            return {'status': False, 'message':'Se genero una excepcion al inicializar la conexion con deriv: '+str(err)}
        
        return await self.check_deriv()

    async def get_balance(self):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            balance_response = await self.api.balance()

            balance_info = balance_response.get("balance")

            account_type = "real" if balance_info.get("account_type") == "real" else "demo"

            balance_amount = balance_info.get("balance")

            return {
                'status': True,
                'message': f"Balance obtenido correctamente",
                'account_type': account_type,
                'balance': balance_amount
            }
        
        except Exception as err:

            return {'status': False, 'message': f"Error al obtener balance: {err}"}
        
    async def get_candles(self, symbol, count=31, granularity=60):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            candles_response = await self.api.ticks_history({
                "ticks_history": symbol,  
                "count": count,           
                "end": "latest",          
                "style": "candles",       
                "granularity": granularity 
            })

            candles = candles_response.get("candles", [])

            return {
                'status': True,
                'message': f'{len(candles)} velas obtenidas correctamente',
                'candles': candles
            }

        except Exception as err:

            return {'status': False, 'message': f'Error al obtener velas: {err}'}

    def get_loops(self):
        
        return False
    
    async def close_deriv(self):

        if self.api:

            try:

                await self.api.disconnect()

                return {'status': True, 'message': 'Conexión con Deriv cerrada correctamente'}
            
            except Exception as err:

                return {'status': False, 'message': f'Se generó una excepción al cerrar la conexión con Deriv: {err}'}
            
        else:

            return {'status': False, 'message': 'No hay conexión activa para cerrar'}
        
    async def get_active_symbols(self):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            response = await self.api.active_symbols({"active_symbols": "full"})
            
            if "active_symbols" in response:

                active_symbols = response["active_symbols"]

                return {
                    'status': True,
                    'message': f'{len(active_symbols)} activos obtenidos correctamente',
                    'symbols': active_symbols
                }
            
            else:

                return {'status': False, 'message': 'No se encontraron activos disponibles'}
            
        except Exception as err:

            return {'status': False, 'message': f'Error al obtener activos: {err}'}
        
    def get_proposal_data(self,amount,contract_type,duration,duration_unit,symbol):

        return {
                "proposal": 1,
                "amount": amount,
                "basis": self.get_proposal_env_basis(),
                "contract_type": contract_type,
                "currency": self.get_proposal_env_currency(),
                "duration": duration,
                "duration_unit": duration_unit,
                "symbol": symbol
            }

    async def generate_proposal(self, symbol, amount, contract_type, duration, duration_unit, barrier=None, payout=None):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        try:

            if amount <= 0:

                return {'status': False, 'message': 'El monto debe ser mayor que 0'}

            proposal_data = self.get_proposal_data(amount,contract_type,duration,duration_unit,symbol)

            proposal_response = await self.api.proposal(proposal_data)

            if proposal_response is None:

                return {'status': False, 'message': 'La respuesta de la API es None'}

            if 'proposal' in proposal_response:

                return {
                    'status': True,
                    'message': 'Propuesta generada correctamente',
                    'proposal_id': proposal_response["proposal"]["id"],
                    'proposal_details': proposal_response,
                }
            
            else:

                error_message = proposal_response.get("error", {}).get("message", "Respuesta desconocida")

                return {'status': False, 'message': f'Error al generar la propuesta: {error_message}'}

        except Exception as err:

            return {'status': False, 'message': f'Error al generar la propuesta: {err}'}
        
    async def execute_proposal(self, proposal_id):

        if self.api is None:

            return {'status': False, 'message': 'API no inicializada'}

        if proposal_id is None:

            return {'status': False, 'message': 'proposal_id es None'}

        try:

            execution_response = await self.api.buy({"buy": proposal_id, "price": 100})

            if execution_response is None:

                return {'status': False, 'message': 'La respuesta de la API es None'}

            if 'buy' in execution_response:

                return {
                    'status': True,
                    'message': 'Posición ejecutada correctamente',
                    'execution_details': execution_response,
                }
            
            else:

                error_message = execution_response.get("error", {}).get("message", "Respuesta desconocida")

                return {'status': False, 'message': f'Error al ejecutar la posición: {error_message}'}

        except Exception as err:
            
            return {'status': False, 'message': f'Error al ejecutar la posición: {err}'}
        
    async def check_position_result(self, contract_id):

        if self.api is None:
            
            return {'status': False, 'message': 'API no inicializada'}

        try:

            response = await self.api.proposal_open_contract(
                {"proposal_open_contract": 1, "contract_id": contract_id}
            )
            if not response or 'proposal_open_contract' not in response:

                return {'status': False, 'message': 'La respuesta no contiene información válida sobre el contrato'}

            contract_info = response['proposal_open_contract']

            if not contract_info.get('is_sold'):

                return {'status': False, 'message': 'El contrato aún no ha sido vendido o completado'}

            status = contract_info.get('status', 'unknown')

            profit_or_loss = contract_info.get('profit', 0)

            if status == 'won':
                
                return self.get_won_contract(profit_or_loss, contract_info)
            
            elif status == 'lost':

                return self.get_lost_contract(profit_or_loss, contract_info)
            
            else:

                return {'status': False, 'message': f'Estado desconocido: {status}'}

        except Exception as err:

            return {'status': False, 'message': f'Error al consultar contrato: {err}'}

    def get_won_contract(self, profit, contract_info):

        return {
            'status': True,
            'message': 'La posición fue exitosa',
            'profit': profit,
            'contract_details': contract_info,
        }

    def get_lost_contract(self, loss, contract_info):

        return {
            'status': False,
            'message': 'La posición fue perdedora',
            'loss': loss,
            'contract_details': contract_info,
        }








