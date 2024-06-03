# Backend

## Recommended IDE Setup

PyCharm + docker service tab

## Project setup

```sh
docker compose up --build -d
```


### Steps to initial container setup

1) Create settings.py in magnolia folder, and then set up these variables:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL =
EMAIL_HOST = 
EMAIL_PORT = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD =
``` 
or
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
2) Run these commands to setup database:
```sh
docker compose exec backend python manage.py makemigrations
```

```sh
docker compose exec backend python manage.py migrate
```
```sh
docker compose exec backend python manage.py createsuperuser
```

Api located at `localhost:8000`