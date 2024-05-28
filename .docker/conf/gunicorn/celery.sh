#!/bin/bash

DJANGODIR=/application
cd ${DJANGODIR}
export PYTHONPATH=${DJANGODIR}:${PYTHONPATH}
if [ -n "$NORELOAD" ]; then
	    PARAMS="--noreload"
fi

rm celerybeat-schedule &
celery -A celery_app purge -f &
celery -A celery_app beat &
celery -A celery_app flower --port=7999 &
celery -A celery_app worker -c 2 -O fair

