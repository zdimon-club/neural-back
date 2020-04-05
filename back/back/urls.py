# author zdimon77@gmail.com

from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from main.views import index

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="NEURO API",
      default_version='v1',
      description="Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zdimon77@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from account.views.auth import CustomAuthToken, LogoutView


urlpatterns = [

    # path('', index),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', admin.site.urls),

    # REST points




    path('v1/', include([
      path('account/', include('account.urls')),
      path('authsocial/', include('authsocial.urls')),
      path('userlist/', include('userlist.urls')),
      path('usermedia/', include('usermedia.urls')),
    ])),
    
]

if DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)



def clear_online():
   from online.models import UserOnline
   try:
      UserOnline.objects.all().delete()
   except:
      pass

