from django.urls import path, include
from rest_framework import routers
from educational_content.views import eBookViewSet

router = routers.DefaultRouter()
# router.register(r'folders', FolderViewSet)
# router.register(r'files', FileViewSet)
# router.register(r'book_categories', BookCategoryViewSet)
# router.register(r'books', BookViewSet)
router.register(r'ebooks', eBookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('files-in-folder/<int:folder_id>/', FileByFolderListView.as_view())
]