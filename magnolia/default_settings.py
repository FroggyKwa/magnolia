import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = os.getenv('DJANGO_DEBUG')
ALLOWED_HOSTS = [os.getenv('DJANGO_ALLOWED_HOSTS'), ]
CSRF_TRUSTED_ORIGINS = [os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS'), 'http://localhost:8080', 'http://localhost:8000']
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
APPEND_SLASH = True
SESSION_COOKIE_HTTPONLY = False
CSRF_HEADER_NAME = "X-CSRFToken"
INTERNAL_IPS = ["127.0.0.1", '*']

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'search',
    'users',
    'celery_app',
    'emails'
]

REST_FRAMEWORK = dict(
    DEFAULT_FILTER_BACKENDS=['django_filters.rest_framework.DjangoFilterBackend'],
    DATE_INPUT_FORMATS=["%d/%m/%Y", "%Y-%m-%d"],
    DATE_FORMAT="%d/%m/%Y",
    DEFAULT_AUTHENTICATION_CLASSES=[
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'magnolia.urls'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://0.0.0.0:8000",
    "http://localhost:8080",
]

CORS_ALLOW_CREDENTIALS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'magnolia.wsgi.application'
ASGI_APPLICATION = 'magnolia.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'database',
        'PORT': os.getenv('MYSQL_PORT', '3306'),
    }
}

LOGGING = dict(
    version=1, disable_existing_loggers=False,
    formatters=dict(
        verbose=dict(
            format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            datefmt="%d/%b/%Y %H:%M:%S"
        ),
        simple=dict(format='%(levelname)s %(message)s')
    ),
    handlers=dict(
        file={'level': 'ERROR', 'class': 'logging.FileHandler', 'filename': 'magnolia.log', 'formatter': 'verbose'}),
    loggers=dict(
        django=dict(handlers=['file'], propagate=True, level='INFO'),
        MYAPP=dict(handlers=['file'], level='INFO')
    )
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = ['frontend/dist', ]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT')) if os.getenv('EMAIL_PORT').isdigit() else None
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

AUTH_USER_MODEL = 'users.User'
