from django.contrib import admin
from .models import ServiceFAQ


@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ("order", "question")
    list_display_links = ("question",)
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ("question",)