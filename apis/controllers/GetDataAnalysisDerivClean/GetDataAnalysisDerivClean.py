import apis.services.deriv.de_core as de_core

class controller_get_data_analysis_deriv_clean():

    de = None

    def __init__(self):

        self.de = de_core.de_core()

    def init_broker(self):

        return self.de.init_deriv()

    def get_data_analysis_deriv_clean(self):

        result = self.init_broker()

        return result