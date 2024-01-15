from django import forms
from .models import Item

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

