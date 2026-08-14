from rest_framework.generics import ListAPIView
from .models import Stat
from .serializers import StatSerializer

class StatListView(ListAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer