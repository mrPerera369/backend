from django.db import models


class Expectation(models.Model):
    question = models.CharField(max_length=200, help_text="e.g. A free consultation and quotation, always")
    answer = models.TextField(help_text="e.g. Every engagement starts with...")
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1,2...)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    quote = models.TextField(help_text="The testimonial text")
    name = models.CharField(max_length=100, default="Client Name")
    role = models.CharField(max_length=100, help_text="e.g. Project Manager")
    company = models.CharField(max_length=100, help_text="e.g. Commercial Project")
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1,2...)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.role}"