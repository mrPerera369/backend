from django.db import models


class Project(models.Model):
    class Category(models.TextChoices):
        COMMERCIAL = "commercial", "Commercial"
        HEALTHCARE = "healthcare", "Healthcare"
        RESIDENTIAL = "residential", "Residential"
        RETAIL = "retail", "Retail"
        INFRASTRUCTURE = "infrastructure", "Infrastructure"
        INDUSTRIAL = "industrial", "Industrial"

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
    )
    company = models.CharField(max_length=150, help_text="e.g. ABC Developments")
    status = models.CharField(
        max_length=100,
        default="Case study coming soon",
        help_text="e.g. Case study coming soon / View Case Study / Completed 2025",
    )
    description = models.TextField(
        help_text="e.g. Office fit-out and refurbishment for a 12-storey commercial tower."
    )
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Optional. Leave empty to show 'No Photo' placeholder.",
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1,2...)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.company} ({self.category})"