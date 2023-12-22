from django import forms
from .models import Folder, File, BookCategory, Book, eBook

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['label', 'owner']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['label', 'inFolder', 'attachement']

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['label']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['label', 'author', 'code_isbn', 'location', 'attachement', 'sector']

class eBookForm(forms.ModelForm):
    class Meta:
        model = eBook
        fields = ['title', 'author', 'sector', 'career', 'photo_cover', 'attachement', 'is_private']
