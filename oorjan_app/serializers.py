from rest_framework import serializers
from .models import SolarData


class SolarDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarData
        fields = ('installation_key', 'dc_power', 'timestamp')

