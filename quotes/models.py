from django.db import models


class QuoteRequest(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Quote Request"
        verbose_name_plural = "Quote Requests"

    def __str__(self):
        return f"{self.name} - {self.service} ({self.created_at:%Y-%m-%d})"