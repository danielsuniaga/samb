import apis.repositories.api as repository_apis

from decouple import config

class cases_api:

    def __init__(self,cursor):

        self.api = repository_apis.repositories_api(cursor)

        self.api_key = config("API")

    def get_api_result(self):
        
        return self.api.get()
    
    def get_api_key(self,request):

        return self.api.get_api_key(self.api_key,request.headers.get(self.api_key)) if self.api_key in request.headers else {'status':False,'msj': "No se envio la key"}
