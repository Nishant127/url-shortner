from .views import UrlShortnerView
from django.urls import path

urlpatterns = [path("", UrlShortnerView.as_view(), name="url-shortner")]
