python /code/manage.py collectstatic 
python /code/manage.py migrate 
gunicorn coonva.wsgi --bind 0.0.0.0:8000 