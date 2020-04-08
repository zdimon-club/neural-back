
from rest_framework import serializers

class ShortUserSerializer(serializers.Serializer):
    country_string = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    id = serializers.IntegerField(required=True)
    username = serializers.CharField(source='publicname')
    last_name = serializers.CharField()
    main_photo = serializers.CharField()
    main_photo_middle = serializers.CharField()
    age = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    language = serializers.CharField()
    is_online = serializers.BooleanField()
    account = serializers.CharField()
    is_camera = serializers.BooleanField()
    birthday = serializers.DateField()
    gender = serializers.CharField()
    is_verified = serializers.BooleanField()
    get_token = serializers.CharField()
    about_me = serializers.CharField()

    def get_country_string(self,obj):
        return obj.get_country_display()

    def get_is_subscribed(self,obj):
        from account.models import UserProfile
        user_id = self.context.get("user_id")
        if user_id:
            user = UserProfile.objects.get(pk=user_id)
            print(user)
            return user.check_subscription(obj)
        else:
            return False


class UserListItemSerializer(serializers.Serializer):
    country_string = serializers.SerializerMethodField()
    main_photo = serializers.SerializerMethodField()
    middle_photo = serializers.CharField()
    id = serializers.IntegerField(required=True)
    username = serializers.CharField(source='publicname')
    last_name = serializers.CharField()
    main_photo = serializers.CharField()
    age = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    language = serializers.CharField()
    is_online = serializers.BooleanField()
    about_me = serializers.CharField()
    def get_country_string(self,obj):
        return obj.get_country_display()
    def get_main_photo(self,obj):
        return obj.middle_photo()