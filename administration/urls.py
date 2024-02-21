from django.urls import path

from administration.views import IndexView, SchoolsView, AddSchoolView

app_name = 'administration'
urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),

    path(route='établissements/', view=SchoolsView.as_view(), name='schools'),
    path(route='établissements/ajouter/', view=AddSchoolView.as_view(), name='add_school'),
]
