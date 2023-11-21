from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finorg.settings')
app = Celery('finorg')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# from django.conf import settings

# app = Celery('finorg')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'update-news-every-minute': {
        'task': 'newapp.views.update_news_for_all_organizations',
        'schedule': crontab(minute='*'),
    },
}