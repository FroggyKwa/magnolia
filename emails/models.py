import os
import random

import binascii
from django.db import models

from users.models import User


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, related_name='otp', on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True, primary_key=True)
    expiration_date = models.DateTimeField()

    @property
    def code(self):
        return self.token[-6:]

    @staticmethod
    def generate_token(min_length=32, max_length=128):
        length = random.randint(min_length, max_length)
        return binascii.hexlify(
            os.urandom(max_length)
        ).decode()[0:length]

    class Meta:
        db_table = 'one_time_passwords'
