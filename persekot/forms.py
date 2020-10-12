from django import forms

from .models import Karyawan, Persekot, PetanggungJawabanPersekot


class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ('nama',
                  'npk',
                  'unit_kerja',
                  'no_hape',
                  'email',
                  'photo')

        widgets = {
            'npk': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan NPK anda', }),
            'nama': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan nama anda', }),
            'unit_kerja': forms.Select(
                attrs={'class': 'form-control'}),
            'no_hape': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan nomor handpone anda', }),
            'email': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan email anda', }),
        }
