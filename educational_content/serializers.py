from rest_framework import serializers

from educational_content.models import eBook


# class FolderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Folder
#         fields = '__all__'

# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = '__all__'


# class BookCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookCategory
#         fields = '__all__'


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'


class eBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = eBook
        fields = '__all__'