from rest_framework import serializers
from .models import Expectation, Testimonial


class ExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expectation
        fields = ["id", "question", "answer"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "quote", "name", "role", "company"]