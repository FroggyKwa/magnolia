from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('email_confirmed', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        user = self.create_user(email, password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError('Email address is required!')
        email = self.normalize_email(email)
        if password is not None:
            user = self.model(email=email, password=password,
                              **other_fields)
            user.save()
        else:
            user = self.model(email=email, password=password,
                              **other_fields)
            user.set_unusable_password()
            user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(blank=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False, verbose_name="Is email confirmed")
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.email if self.fullname == '' else self.fullname
