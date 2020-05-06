from django.contrib import admin
from django.urls import path, re_path
from stahooServer import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from stahooServer.urls import urlpatterns as stahoo_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Stahoo API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@stahoo.local"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

swagger_urls = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/get_user', views.GetCurrentUserView.as_view(), name='get_current_user'),
    path('api/token/get_user/friends_serialized', views.GetUserWithSerializedFriendsView.as_view(), name='get_user_serialized_friends')
] + stahoo_urls + swagger_urls
