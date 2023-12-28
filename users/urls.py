from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import ConfirmEmailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import ConfirmEmailView
from  .views import LoginView  
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
 
    path('auth/', include('dj_rest_auth.urls')),
 
    path('auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
 
    path('auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    # Login view (replace TokenObtainPairView with LoginView)
    path('api/token/', LoginView.as_view(), name='login'),
 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     #path('api/tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     
]
