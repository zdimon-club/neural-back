from .woman import approve_woman_profile

from .photo import approve_photo, delete_photo, notdelete_photo
from .video import approve_video, notdelete_video, delete_video
from .feed import approve_feed
from .verify_doc import approve_verify_doc

from .agency import approve_agency_profile
from moderation.models import Moderation
import json

import redis
redis_client = redis.Redis(host='localhost', port=6379, db=4)


def notify_owner(what, user):
    for online in user.get_socket_ids():
        
        data = {
            'task': 'put_to_socket',
            'data': {
                'action': 'server-action:moderate:'+what,
                'socket_id': online.sid,
                'data': []
            }            
        }
        redis_client.publish('notifications',json.dumps(data)) 


def dispatch(id, act):
    obj = Moderation.objects.get(pk=id)
    if act=='approve':
        if obj.type_obj == 'woman-profile':
            approve_woman_profile(obj)
        if obj.type_obj == 'agency':
            approve_agency_profile(obj)
        if obj.type_obj == 'photo-new':
            notify_owner('photo',obj.content_object.user)
            approve_photo(obj)
        if obj.type_obj == 'photo-delete':
            user = obj.content_object.user
            delete_photo(obj)
            notify_owner('photo', user)
        if obj.type_obj == 'video-new':
            notify_owner('video',obj.content_object.user)
            approve_video(obj)
        if obj.type_obj == 'video-delete':
            user = obj.content_object.user
            delete_photo(obj)
            notify_owner('video', user)
        if obj.type_obj == 'feed-new':
            notify_owner('feed',obj.content_object.user)
            approve_feed(obj)
        if obj.type_obj == 'verify-doc':
            # notify_owner('feed',obj.content_object.user)
            approve_verify_doc(obj)
            
    if act == 'disapprove':
        if obj.type_obj == 'photo-delete':
            notdelete_photo(obj)
            notify_owner(obj, obj.content_object.user)
        if obj.type_obj == 'video-new':
            user = obj.content_object.user
            delete_video(obj)
            notify_owner('video', user)
        if obj.type_obj == 'video-delete':
            user = obj.content_object.user
            notdelete_video(obj)
            notify_owner(obj, user)
        else:
            obj.delete()
