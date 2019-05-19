from django.shortcuts import render
from rest_framework import viewsets, views
import stahooServer.models as models
import stahooServer.serializers as serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserRegistrationSerializer
    queryset = models.User.objects.all()
    http_method_names = ['post']


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserGetSerializer
    queryset = models.User.objects.all()
    http_method_names = http_method_names = [
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


class SendInvitationView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        email = request.data['email']
        sender = request.user
        receiver = get_object_or_404(models.User, email=email)

        receiver.pending.add(sender)
        receiver.save()

        return Response({"status": "success"})


class AcceptInvitationView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        sender_id = request.data['sender_id']
        receiver = request.user
        is_accepted = request.data['is_accepted']

        sender = get_object_or_404(models.User, pk=sender_id)

        receiver.pending.remove(sender)

        if is_accepted:
            receiver.friends.add(sender)
            sender.friends.add(receiver)

            receiver.save()
            sender.save()

            return Response({"status": "accepted"})
        return Response({"status": "declined"})

class FriendRemovalView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        friend = get_object_or_404(models.User, pk=request.data['friend_id'])

        user.friends.remove(friend)
        friend.friends.remove(user)

        user.save()
        friend.save()

        return Response({"status": "success"})

class GetCurrentUserView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        return Response(serializers.UserGetSerializer(user).data)