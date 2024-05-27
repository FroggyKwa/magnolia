import datetime

from django.contrib.auth import login, authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.utils import IntegrityError

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
            user, _ = User.objects.get_or_create(email=serializer.validated_data.get("email"))
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


class CheckOTPAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = OTPCheckSerializer(data=data)
            confirmed = serializer.is_valid(raise_exception=True)
            otp = serializer.validated_data["otp"]
            if confirmed:
                otp.user.email_confirmed = True
                otp.user.save()
                authenticate(request)
                login(request, otp.user)
                return Response(data={"status": "OK"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
