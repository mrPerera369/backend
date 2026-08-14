from django.contrib import admin
from .models import Expectation, Testimonial


@admin.register(Expectation)
class ExpectationAdmin(admin.ModelAdmin):
    list_display = ("order", "question")
    list_display_links = ("question",)
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ("question",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "role", "company")
    list_display_links = ("name",)
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ("name", "company", "quote")