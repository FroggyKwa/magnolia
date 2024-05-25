from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False, verbose_name="Is email confirmed")



