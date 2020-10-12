from django.contrib import admin

from . models import Karyawan, Persekot


class KaryawanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'npk', 'unit_kerja', 'no_hape', 'email']


admin.site.register(Karyawan, KaryawanAdmin)


class PersekotAdmin(admin.ModelAdmin):
    list_display = ['karyawan',
                    'tgl_pk', 'nominal', 'keterangan', 'jatuh_tempo']

    search_fields = ('karyawan', 'tgl_pk')
    ordering = ('karyawan', 'tgl_pk')


admin.site.register(Persekot, PersekotAdmin)
