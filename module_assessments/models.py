from django.db import models

from school_management.models import AcademicYear, Career, Sector, Semester, Subject
from user_account.models import Student


class TypeOfEvaluation(models.Model):
    title = models.CharField(max_length=50)
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
    note = models.IntegerField(default=0)
    file = models.FileField(upload_to='bulletins')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"bulletin de {self.student} en {self.career}"
