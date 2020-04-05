from rest_framework import serializers


class BadRequestSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()