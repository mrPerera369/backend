from rest_framework import serializers
from .models import ServiceAreaStat


class ServiceAreaStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAreaStat
        fields = ["value", "label"]