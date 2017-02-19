web: gunicorn oorjan.wsgi --log-file -
worker: celery -A oorjan worker -B --loglevel=info
