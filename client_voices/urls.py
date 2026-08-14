from django.urls import path
from .views import ExpectationListView, TestimonialListView

urlpatterns = [
    path("expectations/", ExpectationListView.as_view(), name="expectations-list"),
    path("testimonials/", TestimonialListView.as_view(), name="testimonials-list"),
]