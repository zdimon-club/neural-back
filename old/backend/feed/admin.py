from django.contrib import admin
from image_cropping import ImageCroppingMixin
from account.admin import superadmin_site

# Register your models here.
from feed.models import UserFeed, UserFeedComment
from feed.models import UserFeedSubscription
# Register your models here.

@admin.register(UserFeed, site=superadmin_site)
class UserFeedAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'user', 'is_approved']
    list_filter = ['user']

# admin.site.register(UserFeed, UserFeedAdmin)

@admin.register(UserFeedComment, site=superadmin_site)
class UserFeedCommentAdmin(admin.ModelAdmin):
    list_display = ['feed', 'user', 'text']
    
# admin.site.register(UserFeedComment, UserFeedCommentAdmin)

@admin.register(UserFeedSubscription, site=superadmin_site)
class UserFeedSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user_subscriber', 'user_destination']