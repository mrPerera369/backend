from django.contrib import admin
from django.utils.html import format_html

from .models import Project, CountryImage


@admin.register(CountryImage)
class CountryImageAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "image_preview",
    )

    search_fields = ("country",)

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:80px; width:120px; '
                'object-fit:cover; border-radius:6px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "country",
        "year",
        "category",
        "status",
    )

    list_display_links = ("company",)

    list_filter = (
        "category",
        "country",
        "year",
        "status",
    )

    ordering = ("-year",)

    search_fields = (
        "company",
        "description",
        "country",
    )