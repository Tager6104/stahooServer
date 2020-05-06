from django.urls import include, path
from rest_framework.routers import DefaultRouter

from stahooServer import views

stahoo_router = DefaultRouter()
stahoo_router.register(r'users', views.UserViewSet)
stahoo_router.register(r'create_user', views.UserRegisterViewSet)
stahoo_router.register(r'operations', views.OperationViewSet)
stahoo_router.register(r'user_operations', views.UserOperationViewSet)
stahoo_router.register(r'partials', views.PartialOperationViewSet)


urlpatterns = [
    path('api_stahoo/', include(stahoo_router.urls)),
]
