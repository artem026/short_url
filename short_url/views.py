import csv

from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer


class UrlListviewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

class UrlShortener(APIView):
    def post(self, request, origin_uri):
        try:
            url = Url.objects.get(url=origin_uri)
        except:
            url = Url(url=origin_uri)
            url.save()
        
        short_url = url.short_url

        return Response(short_url)

class UrlExport(APIView):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)
        fields = Url.objects.all().values_list('url', 'short_url')

        for row in fields:
            writer.writerow(row)

        return response