from django import forms
from .models import Invoice, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'default_amount', 'defaut_quantity', 'is_active', 'analytic_code']
        
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'placeholder': 'ex: Frais scolaire',
                    'required': True

                }
            ),
            'default_amount' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True

                }
            ),
            'defaut_quantity' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True

                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
            'analytic_code': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['student', 'career', 'item', 'payment_status', 'comment']
        widgets = {
            'student': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'career': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'item': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'payment_status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'5',
                    'rows':'5'
                }
            )
        }