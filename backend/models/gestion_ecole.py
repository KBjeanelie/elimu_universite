import os
from django.db import models
from backend.models.user_account import Student, Teacher
from elimu_universite import settings
from elimu_universite.constant import days_of_the_weeks, hours_of_the_day, currencies, systemes, statues


class Etablishment(models.Model):
    name = models.CharField(max_length=120)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    social_address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    bulletin_foot = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=50, choices=currencies)
    système = models.CharField(max_length=50, choices=systemes)
    status_fees = models.CharField(max_length=50, choices=statues)
    subscription_fees = models.FloatField(default=1000)
    re_registration_fees = models.FloatField(default=800)
    
    def __str__(self):
        return f"Etablissement: {self.name}"

# Class representing Academic Year
class AcademicYear(models.Model):
    label = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Academic Year: {self.label}"

# Class representing Academic Level
class Level(models.Model):
    label = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Level: {self.label}"

# Class representing Semester
class Semester(models.Model):
    title = models.CharField(max_length=50)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Semester: {self.title}"

# Class representing Academic Program
class Program(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    program_date = models.DateField(blank=True)
    person_in_charge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to='programmes', blank=True)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Programme : {self.title} par {self.person_in_charge}"
    
    def file_exists(self):
        if self.file:
            return os.path.exists(settings.MEDIA_ROOT / str(self.file))
        return False

# Class representing Document Type
class DocumentType(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Document Type: {self.title}"

# Class representing Sanction Appreciation Type
class SanctionAppreciationType(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sanction Appreciation Type: {self.title}"

# Class representing Document
class StudentDocument(models.Model):
    title = models.CharField(max_length=50)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to='student_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Document: {self.title}"

class TeacherDocument(models.Model):
    title = models.CharField(max_length=50)
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to='teacher_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Document: {self.title}"

# Class representing Group Subject
class GroupSubject(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Group Subject: {self.title}"

# Class representing Sector (Field of Study)
class Sector(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sector: {self.title}"

# Class representing Subject
class Subject(models.Model):
    label = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, blank=True, null=True)
    teacher_in_charge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, blank=True, null=True)
    types = [('obligatory', 'Obligatory'), ('secondary', 'Secondary')]
    type = models.CharField(max_length=12, choices=types)
    subject_group = models.ForeignKey(GroupSubject, on_delete=models.SET_NULL, null=True, blank=True)
    possible_evaluation = models.BooleanField(default=True)
    possible_averaging = models.BooleanField(default=True)
    coefficient = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Matiere : {self.label}"

# Class representing Career (Educational Program/Path)
class Career(models.Model):
    title = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Career: {self.title}"

# Class representing Student Career (Association between students and careers)
class StudentCareer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, blank=True, null=True)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)
    is_registered =  models.BooleanField(default=False)
    is_valid =  models.BooleanField(default=False)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Parcours : {self.student} en {self.career}"

# Class representing Schedule (Class Timetable)
class Schedule(models.Model):
    start_hours = models.CharField(max_length=15, choices=hours_of_the_day)
    end_hours = models.CharField(max_length=15, choices=hours_of_the_day)
    day = models.CharField(max_length=10, choices=days_of_the_weeks)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Class Schedule for: {self.subject}"

# Class representing Sanction Appreciation (Student Discipline)
class SanctionAppreciation(models.Model):
    comment = models.TextField(blank=True)
    type = models.ForeignKey(SanctionAppreciationType, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, blank=True, null=True)
    sanction_date = models.DateField(blank=True, null=True)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Sanction de {self.student} pour {self.comment}"
