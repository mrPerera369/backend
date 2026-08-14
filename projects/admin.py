from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("order", "company", "category", "status", "image_preview")
    list_display_links = ("company",)
    list_editable = ("order",)
    list_filter = ("category",)
    ordering = ("order",)
    search_fields = ("company", "description")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:4px;" />',
                obj.image.url,
            )
        return "No Photo"

    image_preview.short_description = "Preview"