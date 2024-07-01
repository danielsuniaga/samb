import apis.repositories.shedule_another as repositories_shedule_another

from apis.services.ishedule import icases_shedule

class cases_shedule_another(icases_shedule):

    def __init__(self,cursor):

        self.shedule = repositories_shedule_another.repositories_shedule_another(cursor)

    def get_shedule_result(self,hour):
        
        return self.shedule.get(hour)
