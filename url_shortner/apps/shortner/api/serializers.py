from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()
    short_url = serializers.CharField(required=False)
