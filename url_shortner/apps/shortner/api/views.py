from rest_framework.views import APIView
from rest_framework import permissions, response, status, generics
from .serializers import UrlSerializer
from shortner.service import ShortnerService
from django.contrib.sites.models import Site


class UrlShortnerView(APIView):
    serializer_class = UrlSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.data["url"]
        short_url_code = ShortnerService.save_short_url(original_url)
        current_site = Site.objects.get_current()
        short_url = current_site.domain + short_url_code
        return response.Response(
            data={"short_url": short_url}, status=status.HTTP_200_OK
        )

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url = serializer.data["url"]
        short_url_code = short_url.split("/")[-1]
        original_url = ShortnerService.get_original_url(short_url_code)
        return response.Response(
            data={"short_url": original_url}, status=status.HTTP_200_OK
        )

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.data["url"]
        short_url = serializer.data["short_url"]
        short_url_code = short_url.split("/")[-1]
        ShortnerService.update_long_url(short_url_code, original_url)
        return response.Response(
            data={"message": "URL updated successfully"},
            status=status.HTTP_200_OK,
        )
