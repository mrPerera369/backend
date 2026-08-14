from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number")

    def has_add_permission(self, request):
        # Only allow adding if no row exists yet
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Never allow deleting - phone number field should always exist (can be left empty instead)
        return False