from celery.decorators import task
import cv2
from backend.settings import DOMAIN, BASE_DIR
from django.core.files import File
import redis
import json
redis_client = redis.Redis(host='localhost', port=6379, db=4)


@task
def take_pic_from_video(media):
    cam = cv2.VideoCapture(media.video.path)
    ret,frame = cam.read()
    path = '%s/tmp/%s.jpg' % (BASE_DIR,media.id)
    print ('Creating...' + path)
    cv2.imwrite(path, frame)
    with open(path, 'rb') as image:
        media.image.save('%s.jpg'% media.id, File(image), save=True)
        media.save()


@task
def add_notification_comment(instance_id):
    from feed.models import UserFeedComment
    from account.models import UserProfile
    from chat.models import ChatRoom
    from feed.serializers import user_feed_serializer
    from account.user_serializer import ShortUserSerializer
    from notifications.models import Notifications
    from notifications.serializers import notification_serializer
    instance = UserFeedComment.objects.get(pk=instance_id)

    id_user_feed = instance.feed.user_id
    id_user_commented = instance.user.id

    user = UserProfile.objects.get(pk=id_user_feed)
    comment_user = UserProfile.objects.get(pk=id_user_commented)
    room_id = ChatRoom.get_room_or_create(user, comment_user).id
    comment = UserFeedComment.objects.get(pk=instance.id)

    notification = Notifications.objects.create(content_object=instance,
                                                user=user,
                                                abonent=comment_user,
                                                type='comment',
                                                is_readed=False)

    user_serialised = ShortUserSerializer(user).data
    comment = user_feed_serializer(comment)
    notification = notification_serializer(notification)
    for online in user.get_socket_ids():
        
        data = {
            'task': 'put_to_socket',
            'data': {
                'action': 'server-action:add_comment_to_chat_room',
                'socket_id': online.sid,
                'data': {
                    'room_id': room_id,
                    'user': user_serialised,
                    'comment': comment,
                    'notification': notification
                }
            }
        }
        redis_client.publish('notifications', json.dumps(data))



@task
def repost_to_chat(comment_id):
    from feed.models import UserFeedComment
    from chat.models import ChatMessage
    from chat.models import ChatRoom
    comment = UserFeedComment.objects.get(pk=comment_id)
    print(comment)
    reciver = comment.feed.user
    commentator = comment.user
    room = ChatRoom.get_room_or_create(reciver, commentator)
    m = ChatMessage()
    m.type = 'post'
    m.message = 'new post'
    m.user = commentator
    m.room = room
    m.content_object = comment
    m.save()
    print('repost_to_chat Done')


@task
def add_notification_subscription(instance_id):
    from feed.models import UserFeedSubscription
    from account.models import UserProfile
    from notifications.serializers import notification_serializer
    from account.user_serializer import user_serializer
    from chat.models import ChatRoom
    from notifications.models import Notifications
    instance = UserFeedSubscription.objects.get(pk=instance_id)

    user_destination = UserProfile.objects.get(pk=instance.user_destination.id)
    user_subscriber = UserProfile.objects.get(pk=instance.user_subscriber.id)

    room_id = ChatRoom.get_room_or_create(user_destination, user_subscriber).id

    notification = Notifications.objects.create(content_object=instance,
                                                user=user_destination,
                                                abonent=user_subscriber,
                                                type='subscribe',
                                                is_readed=False)

    serialized_user_destination = user_serializer(user_destination)
    user_subscriber = user_serializer(user_subscriber)
    notification = notification_serializer(notification)
    for online in user_destination.get_socket_ids():
        data = {
            'task': 'put_to_socket',
            'data': {
                'action': 'server-action:add_subscription',
                'socket_id': online.sid,
                'data': {
                    'id': instance_id,
                    'user_id': user_destination.id,
                    'user_dest': serialized_user_destination,
                    'user_sub': user_subscriber,
                    'notification': notification
                }
            }
        }

        redis_client.publish('notifications', json.dumps(data))
    print('add_notification_subscription Done')

