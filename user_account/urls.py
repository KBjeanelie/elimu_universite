from django.urls import path, include
from rest_framework import routers
from . import views

from user_account.views import ManagementProfilViewSet, StudentViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'management_profil', ManagementProfilViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('student-account-view/', views.StudentAccountView.as_view(), name="student-account-view"),
    path('teacher-account-view/', views.TeacherAccountView.as_view(), name="teacher-account-view")
]