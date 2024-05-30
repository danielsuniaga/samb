from django.db import models

import uuid

UPDATE_DATE_VERBOSE_NAME = 'Update Date'

REGISTRATION_DATE_VERBOSE_NAME = 'Registration Date'

class samb_apis(models.Model):

    """ REGISTRAMOS TODAS LAS APIS QUE SE GESTIONEN """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    class Meta: 

        verbose_name = 'samb_apis'

        verbose_name_plural = 'samb_apis'

        db_table = 'samb_apis'

    def get_samb_apis(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_apis()

class samb_platform(models.Model):

    """ REGISTRAMOS TODAS LAS PLATAFORMAS CON LAS QUE NOS VAMOS A INTEGRAR """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    class Meta: 

        verbose_name = 'samb_platform'

        verbose_name_plural = 'samb_platform'

        db_table = 'samb_platform'

    def get_samb_platform(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_platform()

class samb_financial_asset(models.Model):

    """ REGISTRAMOS TODAS LOS ACTIVOS FINANCIEROS CON LAS QUE NOS VAMOS A INTEGRAR """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_samb_platform = models.ForeignKey(samb_platform, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_financial_asset'

        verbose_name_plural = 'samb_financial_asset'

        db_table = 'samb_financial_asset'

    def get_samb_financial_asset(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_financial_asset()

class samb_api_financial_asset(models.Model):

    """ REGISTRAMOS TODAS LOS ACTIVOS FINANCIEROS QUE PUEDE GESTIONAR LAS APIS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description', default='EURUSD')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition', default='1')

    id_samb_api = models.ForeignKey(samb_apis, null=True, blank=True, on_delete=models.CASCADE)

    id_samb_financial_asset = models.ForeignKey(samb_financial_asset, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_api_financial_asset'

        verbose_name_plural = 'samb_api_financial_asset'

        db_table = 'samb_api_financial_asset'

    def get_samb_api_financial_asset(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_api_financial_asset()
    
class samb_cronjobs(models.Model):

    """ REGISTRAMOS LA TRAZABILIDAD DE LOS CRONJOBS EJECUTADOS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    start_date = models.CharField(max_length=14, verbose_name='Start Date')

    end_date = models.CharField(max_length=14, verbose_name='End Date')

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_samb_api = models.ForeignKey(samb_apis, null=True, blank=True, on_delete=models.CASCADE)

    id_samb_financial_asset = models.ForeignKey(samb_financial_asset, null=True, blank=True, on_delete=models.CASCADE)

    execution_time = models.CharField(max_length=110, verbose_name='execution_time',default='0')

    def __str__(self):

        texto = "{0} - {1}"

        return texto.format(self.id, self.start_date)

    class Meta: 

        verbose_name = 'samb_cronjobs'

        verbose_name_plural = 'samb_cronjobs'

        db_table = 'samb_cronjobs'

class samb_notification_conditions(models.Model):

    """ REGISTRAMOS TODAS LAS NOTIFICACIONES DE LOS ANALISIS DE LOS DATOS EXTRAIDOS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_samb_cronjobs = models.ForeignKey(samb_cronjobs, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):

        texto = "{0} - {1}"

        return texto.format(self.id, self.description)

    class Meta: 

        verbose_name = 'samb_notification_conditions'

        verbose_name_plural = 'samb_notification_conditions'

        db_table = 'samb_notification_conditions'

class samb_send_message_api_whatsapp(models.Model):

    """ REGISTRAMOS TODOS LOS MENSAJES QUE NOS ENVÍE WHATSAPP """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    id_message_api = models.CharField(max_length=100, verbose_name='cod_message_api')

    recipient_phone_number = models.CharField(max_length=20, verbose_name='Recipient_Phone_Number')

    start_date = models.CharField(max_length=14, verbose_name='Start Date')

    udpate_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_samb_notification_conditions = models.ForeignKey(samb_notification_conditions, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):

        texto = "{0} - {1} - {2}"

        return texto.format(self.id, self.recipient_phone_number, self.start_date)

    class Meta: 

        verbose_name = 'samb_send_message_api_whatsapp'

        verbose_name_plural = 'samb_send_message_api_whatsapp'

        db_table = 'samb_send_message_api_whatsapp'
    
class samb_exceptions_apis(models.Model):

    """ REGISTRAMOS LAS EXCEPCIONES GENERADAS EN LAS APIS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_api = models.ForeignKey(samb_apis, null=True, blank=True, on_delete=models.CASCADE)

    id_platform = models.ForeignKey(samb_platform, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_exceptions_apis'

        verbose_name_plural = 'samb_exceptions_apis'

        db_table = 'samb_exceptions_apis'

    def get_samb_exceptions_apis(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_exceptions_apis()
    
class samb_notifications_exceptions_apis(models.Model):

    """ REGISTRAMOS TODAS LAS NOTIFICACIONES POR CORREO QUE GENEREN LAS EXCEPCIONES REGISTRADAS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=100, verbose_name='Description')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_exceptions_api = models.ForeignKey(samb_exceptions_apis, null=True, blank=True, on_delete=models.CASCADE)

    id_samb_cronjobs = models.ForeignKey(samb_cronjobs, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_notifications_exceptions_apis'

        verbose_name_plural = 'samb_notifications_exceptions_apis'

        db_table = 'samb_notifications_exceptions_apis'

    def get_samb_notifications_exceptions_api(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_notifications_exceptions_api()
    
class samb_notifications_exceptions_apis_independient(models.Model):

    """ REGISTRAMOS TODAS LAS NOTIFICACIONES POR CORREO QUE GENEREN LAS EXCEPCIONES REGISTRADAS INDEPENDIENTE DE LA ESCRITURA DEL CRONJOBS"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=200, verbose_name="Description")

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    id_exceptions_api = models.ForeignKey(samb_exceptions_apis, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = "samb_notifications_exceptions_apis_independient"

        verbose_name_plural = "samb_notifications_exceptions_apis_independient"

        db_table = "samb_notifications_exceptions_apis_independient"

    def get_samb_notifications_exceptions_api_independient(self):

        return "{} - {}".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_notifications_exceptions_api_independient()
    
class samb_shedule(models.Model):

    """ REGISTRAMOS TODAS LOS HORARIOS REGISTRADOS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=200, verbose_name="Description")

    start_date = models.CharField(max_length=14, verbose_name="Start Date")

    end_date = models.CharField(max_length=255, verbose_name="End Date")
    
    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    class Meta: 

        verbose_name = "samb_shedule"

        verbose_name_plural = "samb_shedule"

        db_table = "samb_shedule"

    def get_samb_shedule(self):

        return "{} - {} - {} - {}".format(self.id,self.description,self.start_date, self.end_date)

    def __str__(self):

        return self.get_samb_shedule()
    
class samb_entrys(models.Model):

    """ REGISTRAMOS TODAS LAS ENTRADAS REGISTRADAS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    id_entry_platform = models.CharField(max_length=20, verbose_name="Entry Platform", default="11111111")

    type = models.CharField(max_length=14, verbose_name="Type")

    type_account = models.CharField(max_length=14, verbose_name="Type Account",default="PRACTICE")

    number_candle = models.CharField(max_length=1, verbose_name="Number Candle",default="5")

    condition_entry = models.CharField(max_length=10, verbose_name="Contition Entry",default="CLOSE")

    amount = models.CharField(max_length=14, verbose_name="Amount")

    result_platform = models.CharField(max_length=14, verbose_name="Results Platform",default="NONE")
    
    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    id_samb_cronjobs = models.ForeignKey(samb_cronjobs, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = "samb_entrys"

        verbose_name_plural = "samb_entrys"

        db_table = "samb_entrys"

    def get_samb_entrys(self):

        return "{} - {} - {} - {}".format(self.id,self.type,self.amount, self.result)

    def __str__(self):

        return self.get_samb_entrys()
    
class samb_framework(models.Model):

    """ REGISTRAMOS TESTING MANUALES DE STRESS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=14, verbose_name="Description",default="Test")
    
    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    class Meta: 

        verbose_name = "samb_framework"

        verbose_name_plural = "samb_framework"

        db_table = "samb_framework"

    def get_samb_framework(self):

        return "{} - {} ".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_framework()
    
class samb_config(models.Model):

    """ REGISTRAMOS CONFIG BASIC SAMB """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    key = models.CharField(max_length=10, verbose_name="key",default="api-key")
    
    value = models.CharField(max_length=100, verbose_name="Value")

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    class Meta: 

        verbose_name = "samb_config"

        verbose_name_plural = "samb_config"

        db_table = "samb_config"

    def get_samb_config(self):

        return "{} - {} ".format(self.id,self.key)

    def __str__(self):

        return self.get_samb_config()
    
class samb_indicators(models.Model):

    """ REGISTRAMOS INDICATORS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    description = models.CharField(max_length=100, verbose_name="Description")

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    class Meta: 

        verbose_name = "samb_indicators"

        verbose_name_plural = "samb_indicators"

        db_table = "samb_indicators"

    def get_samb_indicators(self):

        return "{} - {} ".format(self.id,self.description)

    def __str__(self):

        return self.get_samb_indicators()
    
class samb_indicators_entrys(models.Model):

    """ REGISTRAMOS INDICATORS ASOCIATED WITH ENTRYS"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    id_entry = models.ForeignKey(samb_entrys, null=True, blank=True, on_delete=models.CASCADE)

    id_indicators = models.ForeignKey(samb_indicators, null=True, blank=True, on_delete=models.CASCADE)

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")

    value = models.CharField(max_length=20, verbose_name="Value",default="0")

    class Meta: 

        verbose_name = "samb_indicators_entrys"

        verbose_name_plural = "samb_indicators_entrys"

        db_table = "samb_indicators_entrys"

    def get_samb_indicators_entrys(self):

        return "{}".format(self.id)

    def __str__(self):

        return self.samb_indicators_entrys()
    
class samb_movements(models.Model):

    """ REGISTRAMOS TODOS LOS MOVIMIENTOS QUE EXTRAEMOS """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    id_entity_candle = models.CharField(max_length=20, verbose_name='Id entity', default='0')

    from_candle = models.CharField(max_length=20, verbose_name='Open', default='0')

    at_candle = models.CharField(max_length=20, verbose_name='Open', default='0')

    to_candle = models.CharField(max_length=20, verbose_name='Open', default='0')

    open_candle = models.CharField(max_length=20, verbose_name='Open', default='0')

    close_candle = models.CharField(max_length=20, verbose_name='Close', default='0')

    min_candle = models.CharField(max_length=20, verbose_name='Min', default='0')

    max_candle = models.CharField(max_length=20, verbose_name='Max', default='0')

    volume_candle = models.CharField(max_length=20, verbose_name='Max', default='0')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_entry = models.ForeignKey(samb_entrys, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_movements'

        verbose_name_plural = 'samb_movements'

        db_table = 'samb_movements'

    def get_samb_movements(self):

        return "{}".format(self.id)

    def __str__(self):

        return self.get_samb_movements()
    
class samb_movements_analysis(models.Model):

    """ REGISTRAMOS TODAS LOS MOVIMIENTOS QUE ANALIZAMOS POSTERIOR A SU ESCRITURA"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_cronjobs = models.ForeignKey(samb_cronjobs, null=True, blank=True, on_delete=models.CASCADE)
    
    id_movements = models.ForeignKey(samb_movements, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_movements_analysis'

        verbose_name_plural = 'samb_movements_analysis'

        db_table = 'samb_movements_analysis'

    def get_samb_movements_analysis(self):

        return "{} - Fec({})".format(self.id,self.registration_date)

    def __str__(self):

        return self.get_samb_movements_analysis()
    
class samb_send_message_api_telegram(models.Model):

    """ REGISTRAMOS TODAS LOS ENVIOS DE MENSAJES UTILIZANDO TELEGRAM"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    type = models.CharField(max_length=14, verbose_name='Type')

    message = models.CharField(max_length=100, verbose_name='Message')

    chat = models.CharField(max_length=20, verbose_name='Chat')

    response_method = models.CharField(max_length=100, verbose_name='Response Method')

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name='Condition')

    id_cronjobs = models.ForeignKey(samb_cronjobs, null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 

        verbose_name = 'samb_send_message_api_telegram'

        verbose_name_plural = 'samb_send_message_api_telegram'

        db_table = 'samb_send_message_api_telegram'

    def get_samb_send_message_api_telegram(self):

        return "{} - Fec({})".format(self.id,self.message)

    def __str__(self):

        return self.get_samb_send_message_api_telegram()

class samb_reports(models.Model):

    """ REGISTRAMOS TODAS LOS ENVIOS DE REPORTES POR CORREOS"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.CharField(max_length=200, verbose_name="Description")

    registration_date = models.CharField(max_length=14, verbose_name=REGISTRATION_DATE_VERBOSE_NAME)

    update_date = models.CharField(max_length=14, verbose_name=UPDATE_DATE_VERBOSE_NAME)

    condition = models.CharField(max_length=1, verbose_name="Condition")
    class Meta: 

        verbose_name = "samb_reports"

        verbose_name_plural = "samb_reports"

        db_table = "samb_reports"

    def get_samb_reports(self):

        return "{}".format(self.id)

    def __str__(self):

        return self.get_samb_notifications_exceptions_api_independient()