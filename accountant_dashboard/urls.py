from django.urls import path

from accountant_dashboard.views.home_view import AccountantIndexView


urlpatterns = [
    path(route="", view=AccountantIndexView.as_view(), name="index")
]
