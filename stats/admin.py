from django.contrib import admin
from .models import Stat

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("order", "value", "label")
    list_editable = ("value", "label")
    ordering = ("order",)