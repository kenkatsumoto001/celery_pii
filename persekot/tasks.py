from __future__ import absolute_import, unicode_literals
from celery import task
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import requests
# from onesignal import OneSignal, SegmentNotification

from .models import Karyawan, Persekot


@task
def karyawan_created(karyawan_id):
    karyawan = Karyawan.objects.get(id=karyawan_id)
    subject = 'Karyawan dengan NPK nomor. {}'.format(karyawan.npk)
    message = 'Kepada {}, \n\nNPK anda telah dibuat. \
        NPK anda adalah {}.'.format(karyawan.nama,
                                    karyawan.npk)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [karyawan.email])
    return mail_sent


@task
def karyawan_jatuh_tempo(karyawan_id):
    karyawan = Karyawan.objects.get(id=karyawan_id)
    subject = 'Jatuh tempo Persekot untuk karyawan dengan NPK nomor {}'.format(
        karyawan.npk)
    message = 'Kepada {}, \n\nPersekot anda akan jatuh tempo dalam 3 hari. \
        NPK anda adalah {}.'.format(karyawan.nama,
                                    karyawan.npk)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [karyawan.email])
    return mail_sent


@shared_task(name="print_msg_with_name")
def print_message(name, *args, **kwargs):
    print("Celery is working!! {} have implemented it correctly.".format(name))


@shared_task(name="add_2_numbers")
def add(x, y):
    print("Add function has been called!! with params {}, {}".format(x, y))
    return x+y


@task
def send_message():
    client = OneSignal('2f8579b9-55c5-42d1-b2d7-2ac1bafa6bdb',
                       'YzQ3NjU0NTYtYzk0Yy00YjJjLWE0MjUtOTAxOGI0Nzg3ZDE5')

    notification_to_all_active_users = SegmentNotification(
        subtitle={
            'en': 'Kiss :kissing_heart:',
        },
        contents={
            "en": "I Love U :heart:",
        },
        included_segments=SegmentNotification.ACTIVE_USERS,
        big_picture='http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg',
        chrome_big_picture='http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg',
        url='http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg',
    )
    return client.send(notification_to_all_active_users)
