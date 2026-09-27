from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "category",
            "company",
            "country",
            "year",
            "status",
            "description",
            "image",
        ]

    def get_country(self, obj):
        return obj.country.name

    def get_image(self, obj):
        country_image = obj.country_image

        if country_image:
            request = self.context.get("request")

            if request:
                return request.build_absolute_uri(
                    country_image.url
                )

            return country_image.url

        return None