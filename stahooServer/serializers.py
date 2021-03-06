import stahooServer.models as models
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')


class UserSerializedFriendsSerializer(serializers.ModelSerializer):

    class FriendSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = models.User
            fields = ('id', 'username',
                      'email', 'first_name', 'last_name')

    friends = FriendSerializer(many=True, read_only=True)
    pending = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ('id', 'username',
                  'email', 'first_name', 'last_name', 'friends', 'pending')


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username',
                  'email', 'first_name', 'last_name', 'friends', 'pending')


class PartialOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PartialOperation
        fields = ('id', 'amount', 'to_user', 'is_accepted')


class OperationSerializer(serializers.ModelSerializer):
    partials = PartialOperationSerializer(many=True, read_only=True)

    class Meta:
        model = models.Operation
        fields = ('id', 'to_user', 'from_user', 'amount', 'name', 'description',
                  'datetime', 'category', 'cycle_type', 'partials')
