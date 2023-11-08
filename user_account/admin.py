from django.contrib import admin

from user_account.models import ManagementProfil, Student, Teacher, User, UserType

# Register your models here.
admin.site.register(UserType)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ManagementProfil)