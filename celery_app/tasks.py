from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from celery_app.settings import app

logger = get_task_logger(__name__)


@app.task
def send_email(token, email, hostname):
    email_plaintext_message = f"""
    Код: <b>{token.code}</b>
    <br>
    <br>
    Ссылка для входа: 
    {hostname.strip('/')}/reset?token={token}"""

    send_mail(
        "Временный пароль для magnolia",
        email_plaintext_message,
        "froggykwa@yandex.ru",
        [email]
    )
