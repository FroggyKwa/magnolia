import datetime

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from emails.models import OneTimePassword
from users.models import User
from users.serializers import UserSerializer, OTPCheckSerializer


class SignInAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user, _ = User.objects.get_or_create(email=serializer.validated_data.get("email"),
                                                 usertype=serializer.validated_data.get("usertype"))
            token = OneTimePassword.generate_token()
            otp, _ = OneTimePassword.objects.update_or_create(
                user_id=user.id,
                defaults=dict(
                    token=token,
                    expiration_date=timezone.now() + datetime.timedelta(minutes=10)
                )
            )
            return Response(data={"status": "OK"}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class CheckOneTimePasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            if not request.user.is_anonymous:
                return Response(data={"status": "OK"}, status=status.HTTP_200_OK)
            serializer = OTPCheckSerializer(data=data)
            confirmed = serializer.is_valid(raise_exception=True)
            user = get_object_or_404(User, email=serializer.validated_data.get("email"))
            if confirmed:
                user.email_confirmed = True
                user.otp.delete()
                user.save()
                authenticate(request)
                login(request, user)
                return Response(data={"status": "OK"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class WhoAmI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_200_OK, data=UserSerializer(request.user).data)


class LogOutApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = getattr(request.user, 'user', None)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        logout(request)
        return Response(status=status.HTTP_200_OK)
        # return redirect('/')
