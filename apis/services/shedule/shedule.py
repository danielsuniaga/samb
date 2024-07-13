import apis.repositories.shedule.shedule as repository_shedules

from apis.services.shedule.shedule_core import cases_shedule_core

class cases_shedule(cases_shedule_core):

    def __init__(self,cursor):

        super().__init__()

        self.shedule = repository_shedules.repositories_shedule(cursor)