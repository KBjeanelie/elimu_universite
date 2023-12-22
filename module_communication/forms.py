from django import forms
from .models import Information, Event, EventParticipate, Group, GroupMedia

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'date_info', 'content', 'file']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date', 'content', 'file', 'photo']

class EventParticipateForm(forms.ModelForm):
    class Meta:
        model = EventParticipate
        fields = ['student', 'event', 'start_hours', 'end_hours', 'amount']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'career']

class GroupMediaForm(forms.ModelForm):
    class Meta:
        model = GroupMedia
        fields = ['discussion_group', 'legend', 'file']
