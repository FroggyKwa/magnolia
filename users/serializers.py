from django.http import Http404
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from emails.models import OneTimePassword
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email_confirmed = validated_data.get('email_confirmed', instance.email_verified)
        instance.fullname = validated_data.get('fullname', instance.fullname)

    class Meta:
        model = User
        fields = ['id', 'email', 'fullname', 'email_confirmed', 'usertype']


class OTPCheckSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    def validate(self, attrs):
        code = attrs.get('code')
        otp = get_object_or_404(OneTimePassword, token__endswith=code)
        if code == otp.code and otp.user.email == attrs.get('email'):
            return attrs
        raise ValidationError('OTP code does not match', code=status.HTTP_401_UNAUTHORIZED)