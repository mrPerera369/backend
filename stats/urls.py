from django.urls import path
from .views import StatListView

urlpatterns = [
    path("stats/", StatListView.as_view(), name="stats-list"),
]