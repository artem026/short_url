from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer


class UrlListviewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

class UrlShortener(APIView):
    def post (self, request, origin_url):
        try:
            url = Url.objects.get(url=origin_url)
        except:
            url = Url(url=origin_url)
            url.save()
        
        short_url = url.short_url

        return Response(short_url)


