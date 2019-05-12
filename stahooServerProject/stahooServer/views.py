from django.shortcuts import render
from rest_framework import viewsets
import stahooServer.models as models
import stahooServer.serializers as serializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserRegistrationSerializer
    queryset = models.User.objects.all()
    http_method_names = ['post']


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserGetSerializer
    queryset = models.User.objects.all()
    http_method_names = [m for m in super().http_method_names if m != 'post']


class OperationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OperationSerializer
    queryset = models.Operation.objects.all()


class PartialOperationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PartialOperationSerializer
    queryset = models.PartialOperation.objects.all()
