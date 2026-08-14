from django.contrib import admin
from .models import ServiceAreaStat


@admin.register(ServiceAreaStat)
class ServiceAreaStatAdmin(admin.ModelAdmin):
    list_display = ("order", "value", "label")
    list_editable = ("value", "label")
    ordering = ("order",)