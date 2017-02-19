from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.

# will add created datetime to every model
class BaseModel(models.Model):

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True

# have attributes of data coming as post request
class SolarData(BaseModel):

    user_id = models.ForeignKey('SolarMetaData', models.DO_NOTHING, blank=True, null=True)
    dc_power = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "SolarData"
        verbose_name_plural = "SolarData"

    def __unicode__(self):
        return str(self.user_id)


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
        return str(self.id)

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

    email_to = models.EmailField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "ReportAnalyzer"
        verbose_name_plural = "ReportAnalyzer"

    def __unicode__(self):
        return str(self.email_to)
