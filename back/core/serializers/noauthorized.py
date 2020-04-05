from rest_framework import serializers


class NoAuthSerializer(serializers.Serializer):
    detail = serializers.CharField()