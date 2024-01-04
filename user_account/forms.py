from django import forms
from .models import Student, Teacher, ManagementProfil, User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['registration_number', 'lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'email', 'bithday', 'nationality', 'picture']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['lastname', 'firstname', 'address', 'tel', 'city', 'sex', 'bithday', 'nationality', 'email', 'status', 'last_diploma', 'picture', 'type_of_counter', 'start_of_contrat', 'end_of_contrat']

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

