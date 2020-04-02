from django.contrib import admin
from image_cropping import ImageCroppingMixin

# Register your models here.
from feed.models import UserFeed, UserFeedComment
from feed.models import UserFeedSubscription
# Register your models here.

@admin.register(UserFeed)
class UserFeedAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'user', 'is_approved']
    list_filter = ['user']


@admin.register(UserFeedComment)
class UserFeedCommentAdmin(admin.ModelAdmin):
    list_display = ['feed', 'user', 'text']
    

@admin.register(UserFeedSubscription)
class UserFeedSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user_subscriber', 'user_destination']
