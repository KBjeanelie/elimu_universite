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
    path('teacher-account-view/', views.TeacherAccountView.as_view(), name="teacher-account-view"),
    path('manager-account-view/', views.ManagerAccountView.as_view(), name="manager-account-view"),
    path('accountant-account-view/', views.AccountantAccountView.as_view(), name="accountant-account-view"),
]