from django.urls import path

from administration.views import IndexView

app_name = 'administration'
urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index')
]
