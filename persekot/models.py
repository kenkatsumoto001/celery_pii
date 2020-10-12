from django.db import models
from datetime import timedelta
import uuid
import os

UNIT_KERJA = [
    (1, 'Kepesertaan'),
    (2, 'Pelayanan'),
    (3, 'Keuangan'),
    (4, 'Umum & SDM'),
]


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)


class Karyawan(models.Model):
    nama = models.CharField(max_length=50)
    npk = models.CharField(max_length=9)
    unit_kerja = models.IntegerField(choices=UNIT_KERJA)
    no_hape = models.CharField(max_length=12)
    email = models.EmailField()
    photo = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return '%s - %s' % (self.npk, self.nama)


class Persekot(models.Model):
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    keterangan = models.TextField()
    nominal = models.DecimalField(max_digits=13, decimal_places=2)
    tgl_pk = models.DateField()

    def jatuh_tempo(self):
        return self.tgl_pk + timedelta(days=15)


class PetanggungJawabanPersekot(models.Model):
    persekot = models.ForeignKey(Persekot, on_delete=models.CASCADE)
    tgl_selesai_pk = models.DateField()
