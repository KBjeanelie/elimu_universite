from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'donations', views.DonationViewSet, basename='donations')
router.register(r'billing-brackets', views.BillingBracketViewSet, basename='billing-brackets')
router.register(r'timelines', views.TimeLineViewSet, basename='timelines')
router.register(r'items', views.ItemViewSet, basename='items')

urlpatterns = router.urls
