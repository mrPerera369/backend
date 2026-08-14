from rest_framework import serializers
from .models import ServiceFAQ


class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = ["id", "question", "answer"]