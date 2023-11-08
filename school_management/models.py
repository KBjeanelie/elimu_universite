from django.db import models


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

# class Semestrer(models.Model):
#     pass



# class DocumentType(models.Model):
#     pass

# class Document(models.Model):
#     pass

# class GroupSubject(models.Model):
#     pass

# class Subject(models.Model):
#     pass

# class Career(models.Model):
#     pass

# class SanctionAssessmentType(models.Model):
#     pass

# class SanctionAssessment(models.Model):
#     pass

# class Cycle(models.Model):
#     pass

# class StudentCareer(models.Model):
#     pass

# class Classes(models.Model):
#     pass

# class Program(models.Model):
#     pass