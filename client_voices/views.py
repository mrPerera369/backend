from rest_framework.generics import ListAPIView
from .models import Expectation, Testimonial
from .serializers import ExpectationSerializer, TestimonialSerializer


class ExpectationListView(ListAPIView):
    queryset = Expectation.objects.all()
    serializer_class = ExpectationSerializer


class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer