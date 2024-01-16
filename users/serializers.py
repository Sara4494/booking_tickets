from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser, Profile
import os
from django.contrib.auth import get_user_model
from .  import  google
from users.register1 import ergister_social_user
 
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
 
 

from rest_framework import serializers
from .google import Google

class GoogleSociaAuthViewSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)  # Fix method name to 'validate'
        
        # Check if 'sub' key exists and is a string
        if not isinstance(user_data, dict) or 'sub' not in user_data or not isinstance(user_data['sub'], str):
            raise serializers.ValidationError("The token is invalid or expired. Please login again.")

        # Additional validation logic...

        return user_data
 