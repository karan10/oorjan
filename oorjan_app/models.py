from __future__ import unicode_literals

from django.db import models
from helpers.common import Common
import uuid

# Create your models here.

# will add created datetime to every model
class BaseModel(models.Model):

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True

# have attributes of data coming as post request
class SolarData(BaseModel):

    installation_key = models.CharField(max_length=100, blank=True, null=True)
    dc_power = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "SolarData"
        verbose_name_plural = "SolarData"

    def __unicode__(self):
        return str(self.installation_key)


# solar meta data about solar installation
class SolarMetaData(BaseModel):

    TIMEFRAME = ( ('HOURLY', 'HOURLY'), ('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY'), ('YEARLY', 'YEARLY') )

    installation_key = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    system_capacity =  models.IntegerField( blank=True, null=True, help_text='In Kw' )
    azimuth = models.IntegerField( blank=True, null=True )
    array_type = models.IntegerField( blank=True, null=True )
    module_type = models.IntegerField( blank=True, null=True )
    losses = models.IntegerField( blank=True, null=True )
    tilt = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    dataset = models.CharField(max_length=5, blank=True, null=True)
    timeframe = models.CharField(max_length=10, choices=TIMEFRAME, blank=True, null=True)


    class Meta:
        verbose_name = "SolarMetaData"
        verbose_name_plural = "SolarMetaData"

    def __unicode__(self):
        return str(self.installation_key)

# store reference data
class SolarReferenceData(BaseModel):

    dc_power = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "SolarReferenceData"
        verbose_name_plural = "SolarReferenceData"

    def __unicode__(self):
        return str(self.id)



class ReportAnalyzer(BaseModel):

    report_hour = models.IntegerField( choices=[(i, i) for i in range(1, 23)], blank=True, null=True )
    set_urgent_ts = models.BooleanField(default=False)
    urgent_ts = models.DateTimeField(blank=True, null=True)
    email_to = models.EmailField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def save(self):
        super(ReportAnalyzer, self).save()
        if self.set_urgent_ts is True:
            from .tasks import send_urgent_email_report
            send_urgent_email_report.apply_async( eta=Common.local_time_to_utc(self.urgent_ts) )


    class Meta:
        verbose_name = "ReportAnalyzer"
        verbose_name_plural = "ReportAnalyzer"

    def __unicode__(self):
        return str(self.email_to)
