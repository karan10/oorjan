from celery.task import periodic_task
from datetime import timedelta
from cron_jobs.daily_report import EmailReport




@periodic_task(run_every=crontab(hour=20))
def send_email_report():
    obj = EmailReport()
    obj._starter()
