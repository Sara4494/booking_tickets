from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        # افحص بيانات تسجيل الدخول من الطلب
        username = request.data.get('username')
        password = request.data.get('password')

        # قم بالتحقق من بيانات تسجيل الدخول
        if not username or not password:
            return Response(
                {"detail": "Both username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # قم بالتحقق من صحة بيانات تسجيل الدخول واسترجاع المستخدم
            user = CustomUser.objects.get(username=username)
            if not user.check_password(password):
                raise CustomUser.DoesNotExist
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "Unable to log in with provided credentials."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # قم بإنشاء وتوفير الرموز المميزة
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'refresh_token': str(refresh),
            'access_token': access_token,
        })
