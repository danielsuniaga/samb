import apis.repositories.shedule as repository_shedules

class cases_shedule:

    def __init__(self,cursor):

        self.shedule = repository_shedules.repositories_shedule(cursor)

    def get_shedule_result(self,hour):
        
        return self.shedule.get(hour)
