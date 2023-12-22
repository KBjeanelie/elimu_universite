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
