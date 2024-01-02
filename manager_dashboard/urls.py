from django.conf.urls.static import static
from django.urls import path

from elimu_universite import settings
from manager_dashboard.views.home_view import ManagerIndexView


app_name = 'manager_dashboard'
urlpatterns = [
    path(route='', view=ManagerIndexView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)