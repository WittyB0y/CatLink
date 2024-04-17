import os
from celery import Celery

from CatApp import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CatApp.settings")
celery = Celery("CatApp")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.conf.timezone = settings.TIME_ZONE  # Europe/Minsk
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
