from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'persekot'
urlpatterns = [
    path('karyawan/new/', views.karyawan_new, name='karyawan_new'),
    path('karyawan/<int:pk>/edit/', views.karyawan_edit, name='karyawan_edit'),
    path('karyawan/<int:pk>/remove/',
         views.karyawan_remove, name='karyawan_remove'),
    path('karyawan/<int:pk>/', views.karyawan_detail, name='karyawan_detail'),
    path('karyawan/', views.karyawan_list, name='karyawan_list'),
    path('pk_list', views.pk_list, name='pk_list'),
    path('', views.index, name='persekot'),
]
