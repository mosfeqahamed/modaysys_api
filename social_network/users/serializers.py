from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Friend

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['user_from', 'user_to']
