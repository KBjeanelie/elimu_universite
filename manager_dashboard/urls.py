from django.conf.urls.static import static
from django.urls import path

from elimu_universite import settings


app_name = 'manager_dashboard'
urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)