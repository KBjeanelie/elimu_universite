"""elimu_universite URL Configuration """
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from elimu_universite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
