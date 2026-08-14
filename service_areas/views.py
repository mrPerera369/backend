from rest_framework.generics import ListAPIView
from .models import ServiceAreaStat
from .serializers import ServiceAreaStatSerializer


class ServiceAreaStatListView(ListAPIView):
    queryset = ServiceAreaStat.objects.all()
    serializer_class = ServiceAreaStatSerializer