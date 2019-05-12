import stahooServer.models as models
from rest_framework import serializers


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username',
                  'email', 'first_name', 'last_name', 'friends')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user


class PartialOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PartialOperation
        fields = ('id', 'amount', 'to_user', 'is_accepted')


class OperationSerializer(serializers.ModelSerializer):
    partials = PartialOperationSerializer(many=True, read_only=True)

    class Meta:
        model = models.Operation
        fields = ('id', 'to_user', 'from_user', 'amount', 'name', 'description',
                  'datetime', 'operation_type', 'category', 'cycle', 'partials')
