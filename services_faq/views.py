from rest_framework.generics import ListAPIView
from .models import ServiceFAQ
from .serializers import ServiceFAQSerializer


class ServiceFAQListView(ListAPIView):
    queryset = ServiceFAQ.objects.all()
    serializer_class = ServiceFAQSerializer