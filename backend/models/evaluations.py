import os
from django.db import models
from backend.models.gestion_ecole import AcademicYear, Career, Etablishment, Semester, Subject
from backend.models.user_account import Student
from elimu_universite import settings


class TypeOfEvaluation(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(Etablishment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sector: {self.title}"


class Assessment(models.Model):
    note = models.IntegerField(default=0)
    is_publish = models.BooleanField(default=False)
    type_evaluation = models.ForeignKey(TypeOfEvaluation, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    career = models.ForeignKey(Career, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Evaluation {self.subject} de {self.student}, note {self.note}"


class ReportCard(models.Model):
    average = models.FloatField(default=10)
    file = models.FileField(upload_to='releves_notes')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"bulletin de {self.student} en {self.career}"
    
    def file_exists(self):
        if self.file:
            return os.path.exists(settings.MEDIA_ROOT / str(self.file))
        return False

    def delete(self, *args, **kwargs):
        # Supprimer le fichier associé s'il existe
        if self.file and os.path.exists(os.path.join(settings.MEDIA_ROOT, str(self.file))):
            os.remove(os.path.join(settings.MEDIA_ROOT, str(self.file)))
        
        # Supprimer l'objet
        super(ReportCard, self).delete(*args, **kwargs)