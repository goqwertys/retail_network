from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for registration """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer for display user profile """
    class Meta:
        model = User
        fields = ['email']


class UserUpdateSerializer(serializers.ModelSerializer):
    """ Serializer for editing user """
    class Meta:
        model = User
        fields = ['email']
