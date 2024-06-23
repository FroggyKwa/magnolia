from django.http import Http404
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from emails.models import OneTimePassword
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    usertype = serializers.ChoiceField(['ST', 'EN'])

    def create(self, validated_data):
        user, _ = User.objects.update_or_create(email=validated_data['email'],
                                                defaults={'email': validated_data.get('email'),
                                                          'usertype': validated_data.get('usertype', 'EN')})
        return user


    def update(self, instance, validated_data):
        instance.email_confirmed = validated_data.get('email_confirmed', instance.email_verified)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.usertype = validated_data.get('usertype', instance.usertype)
        return instance


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
