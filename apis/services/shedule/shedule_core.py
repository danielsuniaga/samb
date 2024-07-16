
from apis.services.shedule.ishedule_core import icases_shedule_core
class cases_shedule_core(icases_shedule_core):

    shedule=None

    def get_shedule_result(self,hour):
        
        return self.shedule.get(hour)