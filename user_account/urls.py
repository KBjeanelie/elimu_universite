from django.urls import path, include
from rest_framework import routers

from user_account.views import ManagementProfilViewSet, StudentViewSet, TeacherViewSet, UserTypeViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'user_types', UserTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'management_profil', ManagementProfilViewSet)


urlpatterns = [
    path('', include(router.urls)),
]