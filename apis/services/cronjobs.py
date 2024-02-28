import apis.repositories.cronjobs as repository_cronjobs

import uuid

class cases_cronjobs:

    def __init__(self,cursor):

        self.cronjob = repository_cronjobs.repositories_cronjobs(cursor)

    def generate_cronjob_id(self):

        return uuid.uuid4().hex
    
    def add(self,id_cron,fecha):

        return self.cronjob.add(id_cron,fecha)
    
    def set_fields(self,end_date,execute_time,id_cronjobs):
        
        return self.cronjob.set_fields(end_date,execute_time,id_cronjobs)
