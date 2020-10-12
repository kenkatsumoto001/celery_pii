import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pii.settings')

app = Celery('pii')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'karyawan-jatuh-tempo': {
#         'task': 'persekot.tasks.karyawan_jatuh_tempo',
#         'schedule': crontab(minute=1, day_of_week='mon-fri'),
#     },

# # name of the scheduler
# 'add-every-2-seconds': {
#     # task name which we have created in tasks.py

#     'task': 'add_2_numbers',
#     # set the period of running

#     'schedule': 2.0,
#     # set the args

#     'args': (16, 16)
# },
# # name of the scheduler

# 'print-name-every-5-seconds': {
#     # task name which we have created in tasks.py

#     'task': 'print_msg_with_name',

#     # set the period of running

#     'schedule': 5.0,
#     # set the args

#     'args': ("DjangoPY", )
# },
# }
