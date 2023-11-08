from django.contrib import admin

from school_management.models import AdemicYear, Document, DocumentType, Level, Program

# Register your models here.
admin.site.register(AdemicYear)
admin.site.register(Level)
admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(Program)