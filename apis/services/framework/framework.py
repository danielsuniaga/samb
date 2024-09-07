import apis.repositories.framework.framework as repository_framework

from apis.services.framework.iframework import icases_framework

import uuid

class cases_framework(icases_framework):

    events = None

    def __init__(self,cursor):

        self.framework = repository_framework.repositories_framework(cursor)

    def init_events(self,value):

        self.events = value

        return True
    
    def get_events(self):

        return self.events.get_events()
    
    def set_events_fields(self,fields,value):

        self.events.set_events_field(fields,value)

        return True
    
    def get(self):
        
        return True
    
    def add(self,id_framework,date,description):

        return self.framework.add(id_framework,date,description)
    
    def generate_id(self):

        return uuid.uuid4().hex
    
    def test_events(self):

        self.set_events_fields('init_endpoint','TEST')

        return self.get_events()
    
