from celery.task import periodic_task
from datetime import timedelta
from cron_jobs.daily_report import EmailReport
from celery.schedules import crontab
from .models import ReportAnalyzer
from celery.decorators import task


try:
    solar_analyzer = ReportAnalyzer.objects.get()
    h = solar_analyzer.report_hour
except:
    h = 20

@task
def send_urgent_email_report():
    obj = EmailReport()
    obj._starter()


@periodic_task(run_every=crontab(hour=h))
def send_scheduled_email_report():
    obj = EmailReport()
    obj._starter()