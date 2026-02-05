#!/bin/sh
set -e

# Collect static files
python manage.py collectstatic --noinput

# Copy static files to volume
cp -r /code/staticfiles/* /code/staticfiles/ 2>/dev/null || true

# Ensure media directory exists and has correct permissions
mkdir -p /code/media/pfps
chmod -R 755 /code/media

# Run migrations
python manage.py migrate

# Start gunicorn
gunicorn coonva.wsgi:application --bind 0.0.0.0:8080
