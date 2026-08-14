from django.db import models
from django.core.exceptions import ValidationError


class SiteSettings(models.Model):
    email = models.EmailField(
        blank=True,
        help_text="e.g. info@lithavi.com (leave empty to show placeholder text)",
    )
    phone_number = models.CharField(
        max_length=30,
        blank=True,
        help_text="e.g. +94 77 123 4567 (leave empty to show placeholder text)",
    )
    location_map_embed_url = models.URLField(
        max_length=500,
        blank=True,
        help_text=(
            "Paste the Google Maps EMBED url. Go to Google Maps → search your "
            "location → Share → Embed a map → copy the URL inside src=\"...\" "
            "(NOT the normal share link). Leave empty to show Sri Lanka country-level map."
        ),
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def clean(self):
        # Only one SiteSettings row allowed
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Site Settings already exists. Edit the existing one instead of adding a new one.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)