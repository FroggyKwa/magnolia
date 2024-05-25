from django.http import Http404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email) TODO?
        instance.email_verified = validated_data.get('email_verified', instance.email_verified)
        instance.fullname = validated_data.get('fullname', instance.fullname)

    class Meta:
        model = User
        fields = ['email', 'email_confirmed']