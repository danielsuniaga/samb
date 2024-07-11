import apis.repositories.shedule_another as repositories_shedule_another

from apis.services.shedule.shedule_core import cases_shedule_core

class cases_shedule_another(cases_shedule_core):

    def __init__(self,cursor):

        super().__init__()

        self.shedule = repositories_shedule_another.repositories_shedule_another(cursor)
