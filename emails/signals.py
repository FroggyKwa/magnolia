from django.db.models.signals import post_save
from django.dispatch import receiver

from celery_app.tasks import send_email
from emails.models import OneTimePassword


@receiver(post_save, sender=OneTimePassword)
def one_time_password_created(sender, instance, **kwargs):
    send_email.delay(instance, instance.user.email, instance.request.build_absolute_uri('/'))