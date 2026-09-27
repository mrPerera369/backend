from django.db import models
from django_countries.fields import CountryField


class CountryImage(models.Model):
    country = CountryField(
        unique=True,
        blank_label="Select country",
    )
    image = models.ImageField(
        upload_to="country-images/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.country)


class Project(models.Model):
    class Category(models.TextChoices):
        COMMERCIAL = "commercial", "Commercial"
        HEALTHCARE = "healthcare", "Healthcare"
        RESIDENTIAL = "residential", "Residential"
        RETAIL = "retail", "Retail"
        INFRASTRUCTURE = "infrastructure", "Infrastructure"
        INDUSTRIAL = "industrial", "Industrial"

    class Status(models.TextChoices):
        COMPLETED = "completed", "Completed"
        ONGOING = "ongoing", "Ongoing"
        CASE_STUDY = "case_study", "Case Study Coming Soon"

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
    )

    company = models.CharField(
        max_length=150,
        help_text="e.g. ABC Developments",
    )

    country = CountryField(
        blank_label="Select country",
        default="LK",
        help_text="Project country",
    )

    year = models.PositiveIntegerField(
        default=2025,
        help_text="Project year",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CASE_STUDY,
    )

    description = models.TextField(
        help_text="Project description",
    )

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return f"{self.company} ({self.country})"

    @property
    def country_image(self):
        try:
            country_image = CountryImage.objects.get(country=self.country)
            return country_image.image if country_image.image else None
        except CountryImage.DoesNotExist:
            return None