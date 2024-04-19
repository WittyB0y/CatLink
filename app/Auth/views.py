from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from utils.generate_random_password import generate_random_password
from .serializers import (
    UserSerializer,
    ChangePasswordSerializer,
    PasswordResetRequestSerializer,
)
from Tasks.tasks import (
    sent_notification_change_password,
    sent_greetings,
    sent_new_password,
)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
                raise ValidationError({'email': 'This email is already in use.'})

            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            sent_greetings.delay(user.email)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChangePasswordSerializer
    http_method_names = ["put", ]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.request.user.set_password(serializer.validated_data['new_password'])
            self.request.user.save()
            sent_notification_change_password.delay(self.request.user.email)
            return Response(
                {'message': 'Password updated successfully.'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class PasswordResetRequest(generics.CreateAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_object_or_404(User, email=email)
            new_password = generate_random_password()
            user.set_password(new_password)
            sent_new_password.delay(user.email, new_password)
            return Response(
                {'message': 'New password was sent, check email.'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
