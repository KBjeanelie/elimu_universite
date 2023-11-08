from django.db import models
from user_account.models import Student, Teacher
from elimu_universite.constant import days_of_the_weeks, hours_of_the_day


class AdemicYear(models.Model):
    
    label = models.CharField(max_length=50)
    
    start_date = models.DateField()
    
    end_date = models.DateField()
    
    statut = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Année academique : {self.label}"

class Level(models.Model):
    
    label = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Niveau : {self.label}"

class Semester(models.Model):
    
    title = models.CharField(max_length=50)
    
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Semestre : {self.label}"

class Program(models.Model):
    
    title = models.CharField(max_length=50)
    
    description = models.TextField(blank=True)
    
    program_date = models.DateField(blank=True)
    
    person_in_charge = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    file = models.FileField(upload_to='programmes', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

class DocumentType(models.Model):
    
    title = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Type Document : {self.label}"

class SanctionAppreciationType(models.Model):
    
    title = models.CharField(max_length=50)
    
    description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Type Document : {self.label}"

class Document(models.Model):
    
    title = models.CharField(max_length=50)
    
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING)
    
    file = models.FileField(upload_to='documents')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Niveau : {self.title}"

class GroupSubject(models.Model):
    
    title = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Type Document : {self.title}"

class Sector(models.Model):
    
    title = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Fillière : {self.title}"

class Subject(models.Model):
    
    label = models.CharField(max_length=25)
    
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    teacher_in_charge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    
    types = [('obligatoire', 'Obligatoire'), ('secondaire', 'Secondaire')]
    
    type = models.CharField(max_length=12, choices=types)
    
    subject_group = models.ForeignKey(GroupSubject, on_delete=models.SET_NULL, null=True, blank=True)
    
    possible_evaluation = models.BooleanField(default=True)
    
    possible_averaging = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

class Career(models.Model):
    
    title = models.CharField(max_length=50)
    
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Parcours : {self.title}"

class StudentCareer(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True)
    
    academic_year = models.ForeignKey(AdemicYear, on_delete=models.DO_NOTHING)
    
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)

class Schedule(models.Model):
    
    start_hours = models.CharField(max_length=15, choices=hours_of_the_day)
    
    end_hours = models.CharField(max_length=15, choices=hours_of_the_day)
    
    day = models.CharField(max_length=10, choices=days_of_the_weeks)
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Emploi du temp de : {self.subject}"

class SanctionAppreciation(models.Model):
    
    comment = models.TextField(blank=True)
    
    type = models.ForeignKey(SanctionAppreciationType, on_delete=models.CASCADE)
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    career = models.ForeignKey(Career, on_delete=models.DO_NOTHING)
    
    sanction_date = models.DateField()

