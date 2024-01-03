from django.conf.urls.static import static
from django.urls import path

from elimu_universite import settings
from manager_dashboard.views.administration_view import TypeDocumentDeleteView, TypeEvaluationView, TypeDocumentView, TypeSanctionDeleteView, TypeSanctionView, SettingAppView, get_last_document_type, get_last_sanction_type
from manager_dashboard.views.home_view import ManagerIndexView


app_name = 'manager_dashboard'
urlpatterns = [
    path(route='', view=ManagerIndexView.as_view(), name='index'),
    path(route='administration/type_evaluation/', view=TypeEvaluationView.as_view(), name='type_evaluation'),
    
    path(route='administration/type_documents/', view=TypeDocumentView.as_view(), name='type_documents'),
    path(route='administration/type_documents/<int:pk>/delete/', view=TypeDocumentDeleteView.as_view(), name='delete_type_document'),
    path(route='administration/type_documents/last/', view=get_last_document_type),
    
    path(route='administration/type_sanctions/', view=TypeSanctionView.as_view(), name='type_sanctions'),
    path(route='administration/type_sanctions/<int:pk>/delete/', view=TypeSanctionDeleteView.as_view(), name='delete_type_sanction'),
    path(route='administration/type_sanctions/last/', view=get_last_sanction_type),
    
    
    path(route='administration/reglage-general/', view=SettingAppView.as_view(), name='reglage_general'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)