cd /pycharm/DJANGOAPI
nohup gunicorn DJANGOAPI.wsgi:application -c gunicorn.conf.py  &
