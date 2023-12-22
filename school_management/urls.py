from django.urls import path, include
from rest_framework import routers

from school_management.views import AcademicYearViewSet, CareerViewSet, DocumentTypeViewSet, DocumentViewSet, GroupSubjectViewSet, LevelViewSet, ProgramViewSet, SanctionAppreciationTypeViewSet, SanctionAppreciationViewSet, ScheduleViewSet, SectorViewSet, SemesterViewSet, StudentCareerViewSet, SubjectViewSet, TeacherScheduleListView


router = routers.DefaultRouter()
router.register(r'academic_years', AcademicYearViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'document_types', DocumentTypeViewSet)
router.register(r'sanctions_appreciations_types', SanctionAppreciationTypeViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'group_subjects', GroupSubjectViewSet)
router.register(r'sectors', SectorViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'careers', CareerViewSet)
router.register(r'students_careers', StudentCareerViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'sanction_appreciations', SanctionAppreciationViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('teacher-schedule/<int:teacher_id>/', TeacherScheduleListView.as_view(), name='teacher_schedule')
]