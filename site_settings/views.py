from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SiteSettings
from .serializers import SiteSettingsSerializer


class SiteSettingsView(APIView):
    def get(self, request):
        settings_obj = SiteSettings.objects.first()
        if settings_obj:
            serializer = SiteSettingsSerializer(settings_obj)
            return Response(serializer.data)
        # No settings row created yet in admin - return empty default
        return Response({"email": "", "phone_number": "", "location_map_embed_url": ""})