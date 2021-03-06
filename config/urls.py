"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from rest_framework.routers import DefaultRouter
from short_url.views import UrlListviewSet, UrlShortener, UrlExport, UrlView

router = DefaultRouter()
router.register('list/', UrlListviewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^short_url/(?P<origin_uri>.+)$', UrlShortener.as_view()),
    path('export/', UrlExport.as_view()),
    re_path(r'^(?P<hash>.+)$', UrlView.as_view())
]

urlpatterns += router.urls
