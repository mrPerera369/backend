from django.db import models


class Stat(models.Model):
    class LabelChoices(models.TextChoices):
        YEARS = "Years of Excellence", "Years of Excellence"
        PROJECTS = "Projects Completed", "Projects Completed"
        RETENTION = "Client Retention Rate", "Client Retention Rate"
        DELIVERY = "On-Time Delivery", "On-Time Delivery"

    label = models.CharField(
        max_length=100,
        choices=LabelChoices.choices,
        unique=True,
    )
    value = models.CharField(
        max_length=20,
        help_text="Number or short text, e.g. 25, 500, 98, 1K (symbols like + or % danna epa)"
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1,2,3...)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} - {self.label}"