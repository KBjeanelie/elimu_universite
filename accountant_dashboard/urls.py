from django.urls import path
from accountant_dashboard.views.administration_view import AddItemView, EditItemView, ItemView
from accountant_dashboard.views.home_view import AccountantIndexView


app_name = 'accountant_dashboard'
urlpatterns = [
    path(route="", view=AccountantIndexView.as_view(), name="index"),
    
    path(route='administration/articles/', view=ItemView.as_view(), name='items'),
    path(route='administration/articles/ajouter/', view=AddItemView.as_view(), name='add_item'),
    path(route='administration/articles/<int:pk>/editer/', view=EditItemView.as_view(), name='edit_item'),
    path(route='administration/articles/<int:pk>/delete/', view=ItemView.as_view(), name='delete_item'),
    
]
