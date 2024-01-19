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
        widgets = {
            'note': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'is_publish':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
            'type_evaluation':forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'student':forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'subject':forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'career':forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'semester':forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'academic_year':forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class ReportCardForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = ['note', 'file', 'student', 'career', 'semester', 'academic_year']
