from django.contrib import admin

from .models import samb_apis, samb_cronjobs, samb_send_message_api_whatsapp, samb_platform, samb_financial_asset, samb_movements, samb_exceptions_apis, samb_notification_conditions, samb_movements_analysis, samb_api_financial_asset,samb_shedule


# Register your models here.

admin.site.register(samb_apis)

admin.site.register(samb_cronjobs)

admin.site.register(samb_notification_conditions)

admin.site.register(samb_send_message_api_whatsapp)

admin.site.register(samb_platform)

admin.site.register(samb_financial_asset)

admin.site.register(samb_movements)

admin.site.register(samb_exceptions_apis)

admin.site.register(samb_movements_analysis)

admin.site.register(samb_api_financial_asset)

admin.site.register(samb_shedule)

