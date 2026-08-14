from django.urls import path
from .views import ServiceAreaStatListView

urlpatterns = [
    path("service-area-stats/", ServiceAreaStatListView.as_view(), name="service-area-stats-list"),
]