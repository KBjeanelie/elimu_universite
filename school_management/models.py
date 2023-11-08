from django.db import models

from user_account.models import Teacher


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

class SanctionAssessmentType(models.Model):
    
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
        return f"Type Document : {self.title}"

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

# class Career(models.Model):
#     pass



# class SanctionAssessment(models.Model):
#     pass

# class Cycle(models.Model):
#     pass

# class StudentCareer(models.Model):
#     pass

# class Classes(models.Model):
#     pass

