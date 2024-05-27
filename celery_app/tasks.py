from celery import shared_task
from django.db.models import QuerySet
from django.utils import timezone
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from celery_app.settings import app
from emails.models import OneTimePassword

logger = get_task_logger(__name__)


@app.task()
def send_email(token, email, hostname):
    email_plaintext_message = f"""
    Код: <b>{token[-6:]}</b>
    <br>
    <br>
    Ссылка для входа: 
    {hostname.strip('/')}/verify?token={token}"""

    send_mail(
        "Временный пароль для magnolia",
        email_plaintext_message,
        "golovankov.is@mail.ru",
        [email],
        html_message=email_plaintext_message,
    )
    print(f"Sent to {email}")

@app.task
def remove_expired_tokens():
    expired_tokens: QuerySet[OneTimePassword] = OneTimePassword.objects.filter(expiration_date__lt=timezone.now())
    print(f'Total expired tokens: {expired_tokens.count()} will be deleted.', end=' ')
    expired_tokens.delete()
