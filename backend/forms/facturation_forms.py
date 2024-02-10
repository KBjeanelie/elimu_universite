from django import forms
from ..models.facturation import Invoice, Item, Regulations

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


class RegulationsForm(forms.ModelForm):
    class Meta:
        model = Regulations
        fields = ['invoice', 'student', 'payment_method', 'amount_payment', 'comment']
        widgets = {
            'invoice': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'student': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'amount_payment': forms.NumberInput(
                attrs={
                    'type':'number',
                    'class': 'form-control',
                    'required': True
                }
            ),
            'payment_method': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'4',
                    'rows':'2'
                }
            )
        }