"""elimu_universite URL Configuration """
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from elimu_universite import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='ELIMU API')

urlpatterns = [
    re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('user_account/', include('user_account.urls')),
    path('educational_content/', include('educational_content.urls')),
    path('school_management/', include('school_management.urls')),
    path('module_communication/', include('module_communication.urls')),
    path('module_assessments/', include('module_assessments.urls')),
    path('module_invoice_and_accounting/', include('module_invoice_and_accounting.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
