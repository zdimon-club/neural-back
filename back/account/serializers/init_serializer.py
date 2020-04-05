from rest_framework import serializers
from account.user_serializer import ShortUserSerializer
from account.models import UserProfile

class InitSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    token = serializers.CharField()
    language = serializers.CharField(max_length=2)
    user = ShortUserSerializer()
    online = serializers.IntegerField(default=0)
    users_online = serializers.StringRelatedField(many=True)
    ff = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
