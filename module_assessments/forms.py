from django import forms
from .models import TypeOfEvaluation, Assessment, ReportCard

class TypeOfEvaluationForm(forms.ModelForm):
    class Meta:
        model = TypeOfEvaluation
        fields = ['title']

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['note', 'is_publish', 'type_evaluation', 'student', 'subject', 'career', 'semester', 'academic_year']

class ReportCardForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = ['note', 'file', 'student', 'career', 'semester', 'academic_year']
