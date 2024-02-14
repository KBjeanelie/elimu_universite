from django.urls import path
from accountant_dashboard.views.administration_view import AddItemView, EditItemView, ItemView
from accountant_dashboard.views.communication_view import EventsView, InformationsView
from accountant_dashboard.views.facture_comptable_view import EditInvoiceView, FinancialCommitmentView, InvoiceDetailView, InvoiceView
from accountant_dashboard.views.home_view import AccountantIndexView


app_name = 'accountant_dashboard'
urlpatterns = [
    path(route="", view=AccountantIndexView.as_view(), name="index"),
    
    path(route='communication/infomations/', view=InformationsView.as_view(), name='infos'),
    path(route='communication/evenements/', view=EventsView.as_view(), name='events'),
    
    path(route='administration/articles/', view=ItemView.as_view(), name='items'),
    path(route='administration/articles/ajouter/', view=AddItemView.as_view(), name='add_item'),
    path(route='administration/articles/<int:pk>/editer/', view=EditItemView.as_view(), name='edit_item'),
    path(route='administration/articles/<int:pk>/delete/', view=ItemView.as_view(), name='delete_item'),
    
    path(route='factures-&-comptable/factures/', view=InvoiceView.as_view(), name='invoices'),
    path(route='factures-&-comptable/factures/<int:pk>/detail/', view=InvoiceDetailView.as_view(), name='invoice'),
    path(route='factures-&-comptable/factures/<int:pk>/editer/', view=EditInvoiceView.as_view(), name='invoice_edit'),
    path(route='factures-&-comptable/factures/<int:pk>/delete/', view=InvoiceView.as_view(), name='delete_invoice'),
    
    path(route='factures-&-comptable/engagement-financier/', view=FinancialCommitmentView.as_view(), name='financials'),
    
]
