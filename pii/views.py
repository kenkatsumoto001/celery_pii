from django.shortcuts import render
from persekot.tasks import send_message


def index(request):
    # send_message.apply_async(countdown=60)
    return render(request, 'index.html')
