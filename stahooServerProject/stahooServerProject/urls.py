"""stahooServerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from stahooServer import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

stahoo_router = DefaultRouter()
stahoo_router.register(r'users', views.UserViewSet)
stahoo_router.register(r'create_user', views.UserRegisterViewSet)
stahoo_router.register(r'operations', views.OperationViewSet)
stahoo_router.register(r'user_operations', views.UserOperationViewSet)
stahoo_router.register(r'partials', views.PartialOperationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_stahoo/', include(stahoo_router.urls)),

    # ZAPROSZENIA
    path('api_stahoo/send_invitation/',
         views.SendInvitationView.as_view(), name='send_invitation'),
    path('api_stahoo/accept_invitation/',
         views.AcceptInvitationView.as_view(), name='accept_invitation'),
    path('api_stahoo/remove_friend/', views.FriendRemovalView.as_view(), name='remove_friend'),

    # TOKENY
    path('api_stahoo/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api_stahoo/token/refresh',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('api_stahoo/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api_stahoo/token/get_user', views.GetCurrentUserView.as_view(), name='get_current_user'),
    path('api_stahoo/token/get_user/friends_serialized', views.GetUserWithSerializedFriendsView.as_view(), name='get_user_serialized_friends')
]
