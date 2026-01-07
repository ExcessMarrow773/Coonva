python /code/manage.py collectstatic --noinput
python /code/manage.py migrate
ls -fr 2> files.txt
gunicorn coonva.wsgi --bind 0.0.0.0:8000