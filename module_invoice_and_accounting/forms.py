from django import forms
from .models import Item, Invoice, Regulations, FinancialCommitment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'default_amount', 'defaut_quantity', 'is_active', 'analytic_code']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'invoice_date', 'student', 'career', 'item', 'payment_status', 'comment']

class RegulationsForm(forms.ModelForm):
    class Meta:
        model = Regulations
        fields = ['payment_number', 'invoice', 'student', 'payment_method', 'date_payment', 'amount_payment', 'comment']

class FinancialCommitmentForm(forms.ModelForm):
    class Meta:
        model = FinancialCommitment
        fields = ['student', 'school_fees', 'send_date', 'is_send']
