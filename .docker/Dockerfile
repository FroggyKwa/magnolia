FROM python:3.10

RUN rm -rf /application
WORKDIR /application
COPY . .


ENV DJANGO_SETTINGS_MODULE magnolia.settings

RUN pip3 install --no-cache-dir -r /application/requirements/requirements.txt