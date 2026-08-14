from django.db import models


class ServiceFAQ(models.Model):
    question = models.CharField(max_length=255, help_text="e.g. What types of projects do you support?")
    answer = models.TextField(help_text="e.g. We support residential, commercial...")
    order = models.PositiveIntegerField(default=0, help_text="Display order (0,1,2...)")

    class Meta:
        ordering = ["order"]
        verbose_name = "Service FAQ"
        verbose_name_plural = "Service FAQs"

    def __str__(self):
        return self.question