python3 /code/manage.py collectstatic 
python3 /code/manage.py migrate 

cd /code/
ls
.venv/bin/gunicorn coonva.wsgi --bind 0.0.0.0:8000