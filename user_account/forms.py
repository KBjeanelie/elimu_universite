from django import forms
from .models import Student, Teacher, ManagementProfil, User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['registration_number', 'lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'email', 'bithday', 'nationality', 'picture']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'bithday', 'nationality', 'email', 'status', 'last_diploma', 'picture', 'start_of_contrat', 'end_of_contrat']
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
            'last_diploma': forms.TextInput(
                attrs={
                    'type':'text',
                    'class': 'form-control',
                    'placeholder': 'dernier diplôme obtenu',
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
                    "required": True
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
        fields = ['lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'email', 'bio']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'student', 'teacher', 'management_profil', 'is_active', 'is_admin', 'is_manager', 'is_accountant', 'is_student', 'is_teacher']

class UserTeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'teacher', 'is_active', 'is_teacher', 'password']
        
        widgets = {
            'teacher': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'username',
                    'class': 'form-control',
                    'name': 'username',
                    'placeholder': 'kbjeanelie',
                    'required': True

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'id': 'password',
                    'class': 'form-control',
                    'name': 'password',
                    'placeholder': '************',
                    'required': True

                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "required": True
                }
            ),
            'is_teacher': forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "required": True
                }
            ),
        }




class UserStudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'student', 'is_active', 'is_student', 'password']
        
        widgets = {
            'student': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'username',
                    'class': 'form-control',
                    'name': 'username',
                    'placeholder': 'kbjeanelie',
                    'required': True

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'id': 'password',
                    'class': 'form-control',
                    'name': 'password',
                    'placeholder': '************',
                    'required': True

                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "required": True
                }
            ),
            'is_student': forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "required": True
                }
            ),
        }

