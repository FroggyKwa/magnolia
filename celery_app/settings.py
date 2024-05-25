import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magnolia.settings')

app = Celery('magnolia')

app.conf.CELERY_ALWAYS_EAGER = True
app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()