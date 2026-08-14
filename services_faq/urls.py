from django.urls import path
from .views import ServiceFAQListView

urlpatterns = [
    path("services-faq/", ServiceFAQListView.as_view(), name="services-faq-list"),
]