from django import forms
from .models import Information, Event, EventParticipate, Group, GroupMedia
from ckeditor.widgets import CKEditorWidget

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'date_info', 'content', 'file', 'status']
        widgets = {
            'content': CKEditorWidget(),
            'status': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Titre',
                    'required': True
                }
            ),
            'date_info':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                    "required": True
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                }
            ),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date', 'content', 'file', 'status', 'photo']
        widgets = {
            'content': CKEditorWidget(),
            'status': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Titre',
                    'required': True
                }
            ),
            'start_date':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                    "required": True
                }
            ),
            'end_date':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                    "required": True
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                    "required": True
                }
            ),
            'photo': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                    "required": True
                }
            ),
        }

class EventParticipateForm(forms.ModelForm):
    class Meta:
        model = EventParticipate
        fields = ['student', 'event', 'start_hours', 'end_hours', 'amount']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'career']
        
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'placeholder': 'nom du group',
                    'required': True

                }
            ),
            'career': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
        }

class GroupMediaForm(forms.ModelForm):
    class Meta:
        model = GroupMedia
        fields = ['discussion_group', 'legend', 'file']
