#!/bin/sh
set -e

python manage.py collectstatic --noinput
python manage.py migrate

gunicorn coonva.wsgi:application --bind 0.0.0.0:8080
