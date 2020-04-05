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

    #test = serializers.ModelField(model_field=UserProfile.id, many=True)
    #testt = serializers.IntegerField(many=True)

# {
# status: 0
# message: "Ok"
# token: "58d52f5c65e705866e266af6897c9458d5a95770"
# languges: [{id: "ru", name: "Russian"}, {id: "en", name: "English"}]
# user: {country_string: "Ukraine", is_subscribed: false, id: 206, username: "", last_name: "",…}
# users_online: {}
# online: 0
# }