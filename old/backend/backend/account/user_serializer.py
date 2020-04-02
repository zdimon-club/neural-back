
from rest_framework import serializers


def user_serializer(profile):
    from feed.serializers import ShortUserFeedSerializer
    data = {
        "id": profile.id,
        "account": str(profile.account),
        "language": profile.language,
        "gender": profile.gender,
        "username": profile.publicname,
        "email": profile.email,
        "groups": [],
        "is_superuser": profile.is_superuser,
        "main_photo": profile.main_photo,
        "middle_photo": profile.middle_photo,    
        "is_online": profile.is_online,
        "is_camera": profile.is_camera,
        "token": profile.get_token(),
        "last_feed": ShortUserFeedSerializer(profile.getLastFeed()).data     
    }
    return data

class ShortUserSerializer(serializers.Serializer):
    country_string = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
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
    account = serializers.CharField()
    lookingfor = serializers.CharField()
    is_camera = serializers.BooleanField()
    birthday = serializers.DateField()
    gender = serializers.CharField()
    is_verified = serializers.BooleanField()
    goal = serializers.CharField()
    job = serializers.CharField()
    get_token = serializers.CharField()

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