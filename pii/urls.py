from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers

from . import views
from persekot.views import UserViewSet, GroupViewSet, KaryawanViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'karyawan', KaryawanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persekot/', include('persekot.urls', namespace='persekot')),
    path('account/', include('account.urls')),
    path('', views.index, name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('OneSignalSDKWorker.js',
         TemplateView.as_view(template_name='OneSignalSDKWorker.js',
                              content_type='application/x-javascript')),
    path('OneSignalSDKUpdaterWorker.js',
         TemplateView.as_view(template_name='OneSignalSDKUpdaterWorker.js',
                              content_type='application/x-javascript')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
