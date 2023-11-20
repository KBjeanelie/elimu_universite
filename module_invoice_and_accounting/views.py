from rest_framework import viewsets
from module_invoice_and_accounting.models import *
from module_invoice_and_accounting.serializers import *

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class BillingBracketViewSet(viewsets.ModelViewSet):
    queryset = BillingBracket.objects.all()
    serializer_class = BillingBracketSerializer

class TimeLineViewSet(viewsets.ModelViewSet):
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer