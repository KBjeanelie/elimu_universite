from django.contrib import admin

from user_account.models import ManagementProfil, Student, Teacher, User

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ManagementProfil)