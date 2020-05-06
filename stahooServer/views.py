from rest_framework import viewsets
import stahooServer.models as models
import stahooServer.serializers as serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserRegistrationSerializer
    queryset = models.User.objects.all()
    http_method_names = ['post']


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserGetSerializer
    queryset = models.User.objects.all()
    http_method_names = [
        'get', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class OperationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OperationSerializer
    queryset = models.Operation.objects.all()


class UserOperationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OperationSerializer
    queryset = models.Operation.objects.all()
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        user_operations = self.queryset.filter(
            from_user=get_object_or_404(models.User, pk=pk),
            to_user=get_object_or_404(models.User, pk=pk))
        serializer = self.serializer_class(user_operations, many=True)
        return Response(serializer.data)


class PartialOperationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PartialOperationSerializer
    queryset = models.PartialOperation.objects.all()
