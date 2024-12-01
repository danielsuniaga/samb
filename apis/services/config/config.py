from decouple import config

from apis.repositories.config.config import repositories_config

class cases_config:

    cursor = None

    ids = None

    config = None

    nomenclature = None

    def __init__(self,cursor):

        self.cursor = cursor

        self.init_ids()

        self.init_nomenclature()

        self.config = repositories_config(cursor)


    def init_nomenclature(self):

        self.nomenclature = {
            'ope-otc':config("NOMENCLATURE_PAR_OTC"),
            'ope-nom':" ",
            'ope-op':config("NOMENCLATURE_PAR_OP")
        }

    def get_nomenclatura_nom(self):

        return self.nomenclature['ope-nom']
    
    def get_nomenclatura_otc(self):

        return self.nomenclature['ope-otc']

    def get_nomenclatura_op(self):

        return self.nomenclature['ope-op']

    def init_ids(self):

        self.id = {
            'ope-otc':config("OPE_OTC"),
            'ope-nom':config("OPE_NOM"),
            'ope-ope':config("OPE_OPE")
        }

        return True

    def get_id(self,key):

        return self.id[key]

    def set_config(self,id,value):

        return self.config.set_config(id,value)

    def get_config(self,id):

        return self.config.get_config(id)
    
    def get_config_open_otc(self):

        return self.get_config(self.get_id('ope-otc'))
    
    def get_config_open_nom(self):

        return self.get_config(self.get_id('ope-nom'))
    
    def get_config_open_ope(self):

        return self.get_config(self.get_id('ope-ope'))
    
    def set_config_open_otc(self,value):

        return self.set_config(self.get_id('ope-otc'),value)
    
    def set_config_open_nom(self,value):

        return self.set_config(self.get_id('ope-nom'),value)
    
    def set_config_open_ope(self,value):

        return self.set_config(self.get_id('ope-ope'),value)
    
    def check_market_type(self,value,nomenclature):

        if not value['status']:

            return False
        
        if value['data']['value'] == '0':

            return False

        return nomenclature
    
    def init_markets(self):

        return [

            (self.get_config_open_nom(), self.get_nomenclatura_nom()),

            (self.get_config_open_otc(), self.get_nomenclatura_otc()),

            (self.get_config_open_ope(), self.get_nomenclatura_op())

        ]
    
    def check_market(self):

        markets = self.init_markets()
        
        for config, nomenclatura in markets:

            result = self.check_market_type(config, nomenclatura)

            if result:

                return result
            
        return False
