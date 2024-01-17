from django import forms
from .models import Folder, File, BookCategory, Book, eBook

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['label', 'owner']
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'placeholder': 'nom du dossier',
                    'required': True

                }
            ),
            'owner': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
        }

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['label', 'inFolder', 'attachement']
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'placeholder': 'nom du dossier',
                    'required': True

                }
            ),
            'inFolder': forms.HiddenInput(
                attrs={
                    'type':'hidden',
                    "class": "form-control",
                    "required": True
                }
            ),
            'attachement': forms.FileInput(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
        }

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
        fields = ['title', 'author', 'sector', 'career', 'photo_cover', 'attachement']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'placeholder': 'nom du dossier',
                    'required': True

                }
            ),
            'author': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'sector': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'career': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'photo_cover': forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            'attachement': forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
