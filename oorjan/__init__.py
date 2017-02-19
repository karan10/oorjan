
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# add worker: celery -A oorjan worker -B --loglevel=info in Procfile, to make it work

# uncomment below lines to make it work in heroku
# from __future__ import absolute_import, unicode_literals
# from .celery_app import app as celery_app

# __all__ = ['celery_app']