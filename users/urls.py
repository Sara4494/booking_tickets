from django.urls import path, include
 
 
from  .views import *
from rest_framework.authtoken.views import obtain_auth_token
 

urlpatterns = [
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
      path('api-auth',include('rest_framework.urls')),
  
]