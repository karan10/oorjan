from rest_framework import serializers
from .models import SolarData


class SolarDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarData
        fields = ('user_id', 'dc_power', 'timestamp')

