from django.urls import path, include
from rest_framework import routers
from api.views.contenue_pedagogique_views import eBookViewSet
from api.views.user_account_view import AccountantAccountView, ManagementProfilViewSet, ManagerAccountView, StudentAccountView, StudentViewSet, TeacherAccountView, TeacherViewSet

router = routers.DefaultRouter()
# router.register(r'folders', FolderViewSet)
# router.register(r'files', FileViewSet)
# router.register(r'book_categories', BookCategoryViewSet)
# router.register(r'books', BookViewSet)
router.register(r'ebooks', eBookViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'management_profil', ManagementProfilViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('files-in-folder/<int:folder_id>/', FileByFolderListView.as_view())
    
    path('student-account-view/', StudentAccountView.as_view(), name="student-account-view"),
    path('teacher-account-view/', TeacherAccountView.as_view(), name="teacher-account-view"),
    path('manager-account-view/', ManagerAccountView.as_view(), name="manager-account-view"),
    path('accountant-account-view/', AccountantAccountView.as_view(), name="accountant-account-view"),
]