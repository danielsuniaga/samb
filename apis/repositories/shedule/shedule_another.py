from decouple import config

from apis.repositories.shedule.shedule_core import repositories_shedule_core

class repositories_shedule_another(repositories_shedule_core):

    def __init__(self,cursor):

        super().__init__(cursor)

        self.shedule_permission = config("SHEDULE_PERMISSION_ANOTHER")