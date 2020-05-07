from django.urls import include, path
from rest_framework.routers import DefaultRouter

from stahooServer import views

stahoo_router = DefaultRouter()
stahoo_router.register(r'users', views.UserViewSet)
stahoo_router.register(r'operations', views.OperationViewSet)
stahoo_router.register(r'user_operations', views.UserOperationViewSet)
stahoo_router.register(r'partials', views.PartialOperationViewSet)


urlpatterns = [
    path('api/stahoo/', include(stahoo_router.urls)),
    path('api/stahoo/create_user/', views.UserRegisterView.as_view()),
    path('api/stahoo/send_invitation/',
         views.SendInvitationView.as_view(), name='send_invitation'),
    path('api/stahoo/accept_invitation/',
         views.AcceptInvitationView.as_view(), name='accept_invitation'),
    path('api/stahoo/remove_friend/',
         views.FriendRemovalView.as_view(), name='remove_friend'),
]
