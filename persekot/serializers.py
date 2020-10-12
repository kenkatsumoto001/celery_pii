from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Karyawan, Persekot


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class KaryawanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Karyawan
        fields = ['url', 'nama', 'npk', 'unit_kerja',
                  'no_hape', 'email', 'photo']
