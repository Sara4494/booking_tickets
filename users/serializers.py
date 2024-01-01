from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser, Profile
from django.contrib.auth import get_user_model
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "password"]
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'birth_date', 'address']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture', 'favorite_airline', 'preferred_seat']
