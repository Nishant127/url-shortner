from rest_framework.views import APIView
from rest_framework import permissions, response, status, generics
from .serializers import UrlSerializer
from shortner.service import ShortnerService


class UrlShortnerView(APIView):
    serializer_class = UrlSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.data["original_url"]
        ShortnerService.save_short_url(original_url)
        return response.Response(
            data={"message": "Short URL saved successfully"}, status=status.HTTP_200_OK
        )
