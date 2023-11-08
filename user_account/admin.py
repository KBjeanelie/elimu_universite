from django.contrib import admin

from user_account.models import User, UserType

# Register your models here.
admin.site.register(UserType)
admin.site.register(User)