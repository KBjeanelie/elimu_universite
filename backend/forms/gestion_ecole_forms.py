from django import forms
from backend.models.gestion_ecole import *

class EtablishmentForm(forms.ModelForm):
    class Meta:
        model = Etablishment
        fields = ['name', 'tel', 'address', 'social_address', 'email', 'bulletin_foot', 'currency', 'système', 'status_fees', 'subscription_fees', 'month', 're_registration_fees']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                    'required': True
                }
            ),
            'tel' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                    'required': True
                }
            ),
            'address' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                    'required': True
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                    'required': True
                }
            ),
            'social_address' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                }
            ),
            'currency' : forms.Select(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            'bulletin_foot' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'120',
                }
            ),
            'système' : forms.Select(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            'status_fees' : forms.Select(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            'subscription_fees' : forms.NumberInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            're_registration_fees' : forms.NumberInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            'month' : forms.NumberInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                }
            ),
            
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['lastname', 'firstname', 'status', 'blood_type', 'birthday_place', 'allergy', 'address', 'tel', 'city', 'sex', 'email', 'bithday', 'nationality', 'picture']
        widgets = {
            'lastname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Nom',
                    'required': True
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Prenom',
                    'required': True
                }
            ),
            'birthday_place': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Lieu de naissance',
                }
            ),
            'allergy': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'ex: noix de coco; lactose;',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'adresse',
                }
            ),
            'nationality': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Nationalité',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Numéro de téléphone',
                    'required': True
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type':'email',
                    'class': 'form-control',
                    'placeholder': 'email',
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'blood_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sex': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required':True
                }
            ),
            'bithday':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                }
            ),
            'status':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'bithday', 'nationality', 'email', 'status', 'last_diploma', 'picture', 'start_of_contrat', 'end_of_contrat', 'school']
        widgets = {
            'lastname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Nom',
                    'required': True
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Prenom',
                    'required': True
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'adresse',
                }
            ),
            'last_diploma': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nationality': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Nationalité',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Numéro de téléphone',
                    'required': True
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type':'email',
                    'class': 'form-control',
                    'placeholder': 'email',
                    'required': True
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sex': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'bithday':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                }
            ),
            'start_of_contrat':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                }
            ),
            'end_of_contrat':forms.DateInput(
                attrs={
                    'type':'date',
                    "class": "form-control",
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                }
            ),
            'status':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

class ManagementProfilForm(forms.ModelForm):
    class Meta:
        model = ManagementProfil
        fields = ['lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'email', 'bio', 'picture']
        widgets = {
            'lastname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Nom',
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Prenom',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'adresse',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'Numéro de téléphone',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type':'email',
                    'class': 'form-control',
                    'placeholder': 'email',
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sex': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'type':'file',
                    "class": "form-control",
                }
            ),
            'bio':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':5,
                }
            )
        }

class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['label', 'start_date', 'end_date', 'status', 'school']
        widgets = {
            'label' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'50',
                    'placeholder': 'ex: 2020 - 2021',
                    'required': True
                }
            ),
            'start_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'type':'date',
                    'class': 'form-control',
                }
            ),
            'status':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['label', 'fees', 'school']
        widgets = {
            'label' : forms.TextInput(
                attrs={
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'maxLength':'50',
                    'placeholder': 'ex: 1er année',
                    'required': True
                }
            ),
            'fees' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
        }

class SemesterForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['level'].queryset = Level.objects.filter(school=user.school)
    
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
                    'placeholder': 'ex: Semestre 1',
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
    
    def __init__(self, user, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['person_in_charge'].queryset = Teacher.objects.filter(school=user.school)
    
    class Meta:
        model = Program
        fields = ['title', 'description', 'program_date', 'person_in_charge', 'file', 'school']
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
        fields = ['title', 'school', 'status']
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
            ),
            'status':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

class SanctionAppreciationTypeForm(forms.ModelForm):
    class Meta:
        model = SanctionAppreciationType
        fields = ['title', 'description', 'school']

class GroupSubjectForm(forms.ModelForm):
    class Meta:
        model = GroupSubject
        fields = ['title', 'school']
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
        fields = ['title', 'school']
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
    
    def __init__(self, user, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['sector'].queryset = Sector.objects.filter(school=user.school)
        self.fields['teacher_in_charge'].queryset = Teacher.objects.filter(school=user.school)
        self.fields['level'].queryset = Level.objects.filter(school=user.school)
        self.fields['subject_group'].queryset = GroupSubject.objects.filter(school=user.school)
        
    class Meta:
        model = Subject
        fields = ['label', 'coefficient','sector', 'teacher_in_charge', 'level', 'type', 'subject_group', 'possible_evaluation', 'possible_averaging']
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
            'coefficient': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
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
                }
            ),
            'possible_averaging':forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

class CareerForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(CareerForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['sector'].queryset = Sector.objects.filter(school=user.school)
        
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
    def __init__(self, user, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['career'].queryset = Career.objects.filter(sector__school=user.school)
        self.fields['subject'].queryset = Subject.objects.filter(sector__school=user.school)

    class Meta:
        model = Schedule
        fields = ['start_hours', 'end_hours', 'day', 'subject', 'career']
        widgets = {
            'start_hours': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'end_hours': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'day': forms.Select(
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
            'career': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            
        }

class SanctionAppreciationForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(SanctionAppreciationForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['career'].queryset = Career.objects.filter(sector__school=user.school)
        self.fields['subject'].queryset = Subject.objects.filter(sector__school=user.school)
        self.fields['type'].queryset = SanctionAppreciationType.objects.filter(school=user.school)
        student_ids = StudentCareer.objects.filter(academic_year__school=user.school, academic_year__status=True).values_list('student', flat=True).distinct()
        self.fields['student'].queryset = Student.objects.filter(id__in=student_ids)
        
    class Meta:
        model = SanctionAppreciation
        fields = ['comment', 'type', 'subject', 'student', 'career', 'sanction_date', 'school', 'academic_year']
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
                }
            )
        }

class StudentDocumentForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(StudentDocumentForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['document_type'].queryset = DocumentType.objects.filter(school=user.school)
        
    class Meta:
        model = StudentDocument
        fields = ['title', 'document_type', 'file', 'student', 'school']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'Titre du document',
                    'required': True
                }
            ),
            'document_type': forms.Select(
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
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
        }

class TeacherDocumentForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(TeacherDocumentForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['document_type'].queryset = DocumentType.objects.filter(school=user.school)
        
    class Meta:
        model = TeacherDocument
        fields = ['title', 'document_type', 'file', 'teacher', 'school']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'type':'text',
                    'id': 'title',
                    'class': 'form-control',
                    'name': 'title',
                    'maxLength':'50',
                    'placeholder': 'Titre du document',
                    'required': True
                }
            ),
            'document_type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'teacher': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
        }