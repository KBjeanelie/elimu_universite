from rest_framework import serializers

from module_invoice_and_accounting.models import *

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class BillingBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingBracket
        fields = '__all__'

class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = '__all__'


class FinancialCommitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialCommitment
        fields = '__all__'


