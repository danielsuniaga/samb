import apis.repositories.framework as repository_framework

from apis.services.framework.iframework import icases_framework

import uuid

class cases_framework(icases_framework):

    def __init__(self,cursor):

        self.framework = repository_framework.repositories_framework(cursor)

    def get(self):
        
        return True
    
    def add(self,id_framework,date,description):

        return self.framework.add(id_framework,date,description)
    
    def generate_id(self):

        return uuid.uuid4().hex
