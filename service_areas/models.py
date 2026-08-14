from django.db import models


class ServiceAreaStat(models.Model):
    class LabelChoices(models.TextChoices):
        COUNTRIES = "Countries", "Countries"
        CLIENTS = "Clients", "Clients"

    label = models.CharField(
        max_length=100,
        choices=LabelChoices.choices,
        unique=True,
    )
    value = models.CharField(
        max_length=20,
        help_text="Number or short text, e.g. 25, 10K (symbols like + danna epa)"
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1...)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} - {self.label}"