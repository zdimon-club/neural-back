# author zdimon77@gmail.com

from django.contrib import admin
from django.urls import path
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
    path('', index),
    path(r'api-token-auth/', CustomAuthToken.as_view()),

    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
]

if DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

