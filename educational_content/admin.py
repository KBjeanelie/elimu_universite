from django.contrib import admin

from educational_content.models import Book, BookCategory, eBook

# Register your models here.
# admin.site.register(Folder)
# admin.site.register(File)
admin.site.register(BookCategory)
admin.site.register(eBook)
admin.site.register(Book)