import datetime
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import UpdateAPIView
from django.utils import timezone

from module_invoice_and_accounting.models import *
from module_invoice_and_accounting.serializers import *

# class DonationViewSet(viewsets.ModelViewSet):
#     queryset = Donation.objects.all()
#     serializer_class = DonationSerializer

# class BillingBracketViewSet(viewsets.ModelViewSet):
#     queryset = BillingBracket.objects.all()
#     serializer_class = BillingBracketSerializer

# class TimeLineViewSet(viewsets.ModelViewSet):
#     queryset = TimeLine.objects.all()
#     serializer_class = TimeLineSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FinancialCommitmentViewSet(viewsets.ModelViewSet):
    queryset = FinancialCommitment.objects.all()
    serializer_class = FinancialCommitmentSerializer

class FinancialCommitmentUpdateView(UpdateAPIView):
    queryset = FinancialCommitment.objects.all()
    serializer_class = FinancialCommitmentSerializer
    lookup_field = 'pk'
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Mettre à jour send_date avec la date actuelle
            instance.send_date = timezone.now()

            # Mettre is_send à True
            instance.is_send = True

            # Enregistrer les modifications
            instance.save()
            return Response({'message': 'This financial commitment was sent successfully !'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegulationsViewSet(viewsets.ModelViewSet):
    queryset = Regulations.objects.all()
    serializer_class = RegulationsSerializer
    
    def generate_payment_number(self):
        now = datetime.datetime.now()
        year = now.year
        total_regulations = Regulations.objects.count()

        return f"REGL{year}{total_regulations}"
    
    def create(self, request, *args, **kwargs):
        payment_number = self.generate_payment_number()
        request['payment_number'] = payment_number
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer