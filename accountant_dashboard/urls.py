from django.urls import path
from accountant_dashboard.views.administration_view import AddItemView, EditItemView, ItemView
from accountant_dashboard.views.communication_view import EventsView, InformationsView
from accountant_dashboard.views.facture_comptable_view import AddDepenseView, AddRepaymentView, DepenseView, EditDepenseView, EditInvoiceView, EditRepaymentView, FinancialCommitmentView, InvoiceDetailView, InvoiceView, RepaymentView
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
    
    path(route='factures-&-comptable/remboursements/', view=RepaymentView.as_view(), name='repayments'),
    path(route='factures-&-comptable/remboursements/ajouter/', view=AddRepaymentView.as_view(), name='add_repayment'),
    path(route='factures-&-comptable/remboursements/<int:pk>/editer/', view=EditRepaymentView.as_view(), name='edit_repayment'),
    path(route='factures-&-comptable/remboursements/<int:pk>/delete/', view=RepaymentView.as_view(), name='delete_repayment'),
    
    path(route='factures-&-comptable/rapport-des-depenses/', view=DepenseView.as_view(), name='spend'),
    path(route='factures-&-comptable/rapport-des-depenses/ajouter/', view=AddDepenseView.as_view(), name='add_spend'),
    path(route='factures-&-comptable/rapport-des-depenses/<int:pk>/editer/', view=EditDepenseView.as_view(), name='edit_spend'),
    path(route='factures-&-comptable/rapport-des-depenses/<int:pk>/delete/', view=DepenseView.as_view(), name='delete_spend'),
    
    path(route='factures-&-comptable/engagement-financier/', view=FinancialCommitmentView.as_view(), name='financials'),
    
]
