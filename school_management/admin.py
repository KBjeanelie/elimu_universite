from django.contrib import admin

from school_management.models import AdemicYear, Career, Document, DocumentType, GroupSubject, Level, Program, SanctionAssessmentType, Sector, Semester, StudentCareer, Subject

# Register your models here.
admin.site.register(AdemicYear)
admin.site.register(Level)
admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(Program)
admin.site.register(GroupSubject)
admin.site.register(Sector)
admin.site.register(SanctionAssessmentType)
admin.site.register(Subject)
admin.site.register(Career)
admin.site.register(Semester)
admin.site.register(StudentCareer)