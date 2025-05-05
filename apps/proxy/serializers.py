from rest_framework import serializers


class ProxySerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
