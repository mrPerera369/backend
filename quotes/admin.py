from django.contrib import admin
from .models import QuoteRequest


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "email", "service", "email_sent")
    list_filter = ("service", "email_sent", "created_at")
    search_fields = ("name", "email", "company", "message")
    readonly_fields = ("name", "company", "email", "phone", "service", "message", "created_at", "email_sent")
    ordering = ("-created_at",)

    def has_add_permission(self, request):
        # Submissions come from the website form, not manually added in admin
        return False