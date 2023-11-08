from django.contrib import admin

from module_assessments.models import Assessment, ReportCard, TypeOfEvaluation

# Register your models here.
admin.site.register(TypeOfEvaluation)
admin.site.register(Assessment)
admin.site.register(ReportCard)