from django.db import models
from account.models import UserProfile
from image_cropping.fields import ImageRatioField, ImageCropField
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
from django.dispatch import receiver
import os
from back.local import DOMAIN
from django.utils.translation import ugettext_lazy as _

from core.mixins.image import ImageModelMixin
from core.mixins.video import VideoModelMixin
from account.models import UserProfile

#from feed.tasks import add_notification_comment, add_notification_subscription, repost_to_chat



# Create your models here.
from usermedia.models import UserMedia


class UserFeed(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    text = models.TextField()
    geo = models.CharField(max_length=50)
    lon = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    last_media = models.ForeignKey('usermedia.UserMedia', on_delete=models.SET_NULL,  null=True, related_name='lastmedia')

    def __str__(self):
        return self.title

    @property
    def main_media(self):
        try:
            return self.last_media
        except:
            return None

    @property
    def get_video_url(self):
        return DOMAIN + self.video.url

    @property
    def get_middle_url(self):
        return DOMAIN + get_thumbnailer(self.image).get_thumbnail({
            'size': (200, 200),
            'box': self.cropping,
            'crop': 'smart',
            'upscale': True,

        }).url

    @property
    def get_small_url(self):
        return DOMAIN + get_thumbnailer(self.image).get_thumbnail({
            'size': (50, 50),
            'box': self.cropping,
            'crop': 'smart',
            'upscale': True,

        }).url

    @property
    def get_small_img(self):
        try:
            return mark_safe('<img src="%s" />' % self.get_small_url)
        except:
            return None

    @property
    def get_middle_img(self):
        try:
            return mark_safe('<img src="%s" />' % self.get_middle_url)
        except:
            return None



class UserFeedComment(models.Model):
    feed = models.ForeignKey(UserFeed, on_delete=models.CASCADE, blank=False, null=False, related_name='feedcomment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField()
    # text = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_admin_url(self):
        return '/admin/feed/userfeedcomment/%s/change/' % self.id

    class MPTTMeta:
        order_insertion_by = 'id',

    class Meta:
        ordering = ('-id',)


@receiver(models.signals.post_save, sender=UserFeedComment)
def add_message_on_chat(sender, instance, **kwargs):
    repost_to_chat(instance.id)
    add_notification_comment.delay(instance.id)



class UserFeedSubscription(models.Model):
    user_subscriber = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_subscriber')
    user_destination = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_destination')

    class Meta:
        unique_together = ('user_subscriber', 'user_destination',)


@receiver(models.signals.post_save, sender=UserFeedSubscription)
def add_notification_sub(sender, instance, **kwargs):
    add_notification_subscription.delay(instance.id)


@receiver(models.signals.post_delete, sender=UserMedia)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `ImageModel` object is deleted.
    """
    if instance.image:
        try:
            thumbmanager = get_thumbnailer(instance.image)
            thumbmanager.delete(save=False)
            path = instance.image.path
            os.remove(path)
        except:
            pass
    if instance.video:
        try:
            path = instance.video.path
            os.remove(path)
        except:
            pass

@receiver(models.signals.post_save, sender=UserMedia)
def set_video_duration(sender, instance, **kwargs):
    if instance.type_media == 'video' and kwargs['created']:
        instance.duration = instance.get_video_duration()
        instance.save()
