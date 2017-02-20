from django.contrib import admin
from .models import SolarData, SolarMetaData, SolarReferenceData, ReportAnalyzer
# Register your models here.


class SolarDataAdmin(admin.ModelAdmin):
    # readonly_fields=('user_id',)
    list_display=('installation_key', 'timestamp',)

class SolarMetaDataAdmin(admin.ModelAdmin):
    readonly_fields=('installation_key',)


admin.site.register(SolarData, SolarDataAdmin)
admin.site.register(SolarMetaData, SolarMetaDataAdmin)
admin.site.register(SolarReferenceData)
admin.site.register(ReportAnalyzer)

