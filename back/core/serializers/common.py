from rest_framework import serializers


class CommonSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()