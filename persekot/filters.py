import django_filters

from .models import Karyawan, Persekot, PetanggungJawabanPersekot


class KaryawanFilter(django_filters.FilterSet):
    class Meta:
        model = Karyawan
        fields = {
            'npk': ['icontains'],
            'nama': ['icontains'],
            # 'unit_kerja': ['icontains'],
            'no_hape': ['icontains'],
            'email': ['icontains'],
        }
