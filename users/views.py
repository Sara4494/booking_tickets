from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView
from dj_rest_auth.views import LogoutView

from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer, UserLoginSerializer, GoogleSociaAuthViewSerializer

# Custom user details view
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            return Response({
                'status': 'success',
                'message': 'User details retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving user details: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'User details updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating user details: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                'status': 'success',
                'message': 'User deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error deleting user: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            return Response({
                'status': 'success',
                'message': 'Profile details retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving profile details: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Profile details updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating profile details: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                'status': 'success',
                'message': 'Profile deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error deleting profile: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Create or retrieve authentication token
                token, created = Token.objects.get_or_create(user=user)

                # Add the token to the response headers
                response = Response({
                    'status': 'success',
                    'message': 'User logged in successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
                response['Authorization'] = f'Token {token.key}'
                return response
            else:
                return Response({
                    'status': 'error',
                    'message': 'Invalid login credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error logging in: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogoutView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer   
    def create(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response({
                'status': 'success',
                'message': 'User logged out successfully'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error logging out: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserRegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer  

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            login(request, user)
            return Response({
                'status': 'success',
                'message': 'User registered and logged in successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error registering user: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GoogleCallbackView(View):
    def get(self, request, *args, **kwargs):
        # Handle the callback logic here
        return HttpResponse("Google callback handled successfully")
    

 