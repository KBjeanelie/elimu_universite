from rest_framework import viewsets
from educational_content.models import eBook
from api.serializers.contenu_pedagogique_serializer import eBookSerializer

# class FolderViewSet(viewsets.ModelViewSet):
#     queryset = Folder.objects.all()
#     serializer_class = FolderSerializer


# class FileViewSet(viewsets.ModelViewSet):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer


# class BookCategoryViewSet(viewsets.ModelViewSet):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer
#     permission_classes = [IsAuthenticated]


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]


class eBookViewSet(viewsets.ModelViewSet):
    queryset = eBook.objects.all()
    serializer_class = eBookSerializer



# class FileByFolderListView(generics.ListAPIView):
#     serializer_class = FileSerializer

#     def get_queryset(self):
#         folder_id = self.kwargs['folder_id']  # Récupère l'ID du dossier depuis l'URL
#         return File.objects.filter(inFolder_id=folder_id)