import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magnolia.settings')

app = Celery('magnolia')

app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "remove-all-expired-tokens": {
        "task": "celery_app.tasks.remove_expired_tokens",
        "schedule": 10.0,
    }
}