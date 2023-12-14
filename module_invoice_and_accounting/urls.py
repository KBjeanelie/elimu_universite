from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'donations', views.DonationViewSet, basename='donations')
# router.register(r'billing-brackets', views.BillingBracketViewSet, basename='billing-brackets')
# router.register(r'timelines', views.TimeLineViewSet, basename='timelines')
router.register(r'items', views.ItemViewSet, basename='items')
router.register(r'invoices', views.InvoiceViewSet, basename='invoices')
router.register(r'financial-commitment', views.FinancialCommitmentViewSet, basename='financial-commitment')
router.register(r'regulations', views.RegulationsViewSet, basename='regulations')

urlpatterns = [
    path('send-financial-commitment/<int:pk>/', views.FinancialCommitmentUpdateView.as_view())
]
urlpatterns += router.urls
