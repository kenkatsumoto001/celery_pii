from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework import viewsets


from .models import Karyawan, Persekot, PetanggungJawabanPersekot
from .forms import KaryawanForm
from .tasks import karyawan_created, karyawan_jatuh_tempo
from .serializers import (UserSerializer,
                          GroupSerializer,
                          KaryawanSerializer)


def index(request):
    datas = Karyawan.objects.all()
    return render(request, 'persekot/index.html', {'datas': datas})


def karyawan_list(request):
    datas = Karyawan.objects.all()
    return render(request, 'persekot/karyawan_list.html', {'datas': datas})


def karyawan_new(request):
    data_method = {'method': 'New'}
    if request.method == "POST":
        form = KaryawanForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            karyawan_created.delay(post.id)
            karyawan_jatuh_tempo.apply_async((post.id,),
                                             countdown=60)
            return redirect('persekot:karyawan_list')
    else:
        form = KaryawanForm()
    return render(request,
                  'persekot/karyawan_edit.html',
                  {'form': form,
                   'data_method': data_method, })


def karyawan_detail(request, pk):
    datas = get_object_or_404(Karyawan, pk=pk)

    return render(request,
                  'persekot/karyawan_detail.html',
                  {'datas': datas})


def karyawan_edit(request, pk):
    data_method = {'method': 'Edit'}
    data_master = get_object_or_404(Karyawan, pk=pk)
    if request.method == 'POST':
        form = KaryawanForm(request.POST, request.FILES, instance=data_master)
        if form.is_valid():
            data_master = form.save(commit=False)
            data_master.save()
            return redirect('persekot:karyawan_detail', pk=data_master.pk)
    else:
        form = KaryawanForm(instance=data_master)
    return render(request,
                  'persekot/karyawan_edit.html',
                  {'form': form,
                   'data_method': data_method})


def karyawan_remove(request, pk):
    post = get_object_or_404(Karyawan, pk=pk)
    post.delete()
    return redirect('persekot:karyawan_list')


def pk_list(request):
    datas = Persekot.objects.all()

    return render(request, 'persekot/pk_list.html', {'datas': datas})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KaryawanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer
