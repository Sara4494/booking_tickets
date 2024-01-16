from django.urls import re_path  # استبدل استيراد url بـ re_path

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Booking Tickets API",
        default_version='v1',
        description="API for booking tickets",
        terms_of_service="https://yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
 
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('flights.urls')),
    path('user/', include('users.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    path('auth/', include('allauth.socialaccount.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]
 
