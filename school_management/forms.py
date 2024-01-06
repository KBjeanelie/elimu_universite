from django import forms
from .models import (
    AcademicYear,
    Level,
    Semester,
    Program,
    DocumentType,
    SanctionAppreciationType,
    Document,
    GroupSubject,
    Sector,
    Subject,
    Career,
    StudentCareer,
    Schedule,
    SanctionAppreciation,
)

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['label', 'start_date', 'end_date', 'status']
        widgets = {
            'label' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'50',
                    'placeholder': 'Titre du programmme',
                    'required': True
                }
            ),
            'start_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'status':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': True,
                }
            )
        }

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['label']
        widgets = {
            'label' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'50',
                    'placeholder': 'Titre du programmme',
                    'required': True
                }
            ),
        }

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['title', 'level']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'Titre du programmme',
                    'required': True
                }
            ),
            'level': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
        }

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description', 'program_date', 'person_in_charge', 'file']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'placeholder': 'Titre du programmme',
                    'required': True
                }
            ),
            'program_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                }
            ),
            'description' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'description',
                    'cols':"10",
                    'rows':'5'
                }
            ),
            'person_in_charge': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['title']
        labels = {'title': 'Titre'}
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'placeholder': 'cv',
                    'required': True
                }
            )
        }

class SanctionAppreciationTypeForm(forms.ModelForm):
    class Meta:
        model = SanctionAppreciationType
        fields = ['title', 'description']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'document_type', 'file']

class GroupSubjectForm(forms.ModelForm):
    class Meta:
        model = GroupSubject
        fields = ['title']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'ex: Matière scientifique',
                    'required': True
                }
            ),
        }

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['title']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'Nom de la filière',
                    'required': True
                }
            ),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['label', 'sector', 'teacher_in_charge', 'level', 'type', 'subject_group', 'possible_evaluation', 'possible_averaging']
        widgets = {
            'label' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'50',
                    'placeholder': 'Nom de la matière',
                    'required': True
                }
            ),
            'sector': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'teacher_in_charge': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'level': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'subject_group': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'possible_evaluation':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': True,
                }
            ),
            'possible_averaging':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': True,
                }
            )
        }

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['title', 'sector']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'Licence Informatique 1',
                    'required': True
                }
            ),
            'sector': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
        }

class StudentCareerForm(forms.ModelForm):
    class Meta:
        model = StudentCareer
        fields = ['student', 'career', 'academic_year', 'semester']
        

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['start_hours', 'end_hours', 'day', 'subject', 'career']

class SanctionAppreciationForm(forms.ModelForm):
    class Meta:
        model = SanctionAppreciation
        fields = ['comment', 'type', 'subject', 'student', 'career', 'sanction_date']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'description',
                    'cols':"10",
                    'rows':'5'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'subject': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'student': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'career': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'sanction_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'required': True,
                }
            )
        }
