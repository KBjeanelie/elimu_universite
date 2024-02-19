from rest_framework import generics
from api.serializers.model_serializer import AssessmentSerializer
from backend.models.evaluations import Assessment
from rest_framework.permissions import IsAuthenticated

from backend.models.gestion_ecole import AcademicYear

class AssessmentList(generics.ListAPIView):
    serializer_class = AssessmentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        student = user.student
        academic_year = AcademicYear.objects.get(school=user.school, status=True)
        return Assessment.objects.filter(student=student, academic_year=academic_year)

class eBookList(generics.ListAPIView):
    serializer_class = AssessmentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        student = user.student
        academic_year = AcademicYear.objects.get(school=user.school, status=True)
        return Assessment.objects.filter(student=student, academic_year=academic_year)
