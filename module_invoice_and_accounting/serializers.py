from rest_framework import serializers

from module_invoice_and_accounting.models import *
from user_account.serializers import StudentSerializer

# class DonationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Donation
#         fields = '__all__'

# class BillingBracketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BillingBracket
#         fields = '__all__'

# class TimeLineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TimeLine
#         fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_number = serializers.CharField(required=False)
    class Meta:
        model = Invoice
        fields = '__all__'

class RegulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = '__all__'



# class EstimateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Estimate
#         fields = '__all__'



class FinancialCommitmentSerializer(serializers.ModelSerializer):
    send_date = serializers.DateTimeField(required=False, allow_null=True)
    
    class Meta:
        model = FinancialCommitment
        fields = ['id', 'student', 'school_fees', 'send_date']


