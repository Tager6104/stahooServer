from django.shortcuts import render
from rest_framework import viewsets
import stahooServer.models as models
import stahooServer.serializers as serializers

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class OperationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OperationSerializer
    queryset = models.Operation.objects.all()


class PartialOperationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PartialOperationSerializer
    queryset = models.PartialOperation.objects.all()
