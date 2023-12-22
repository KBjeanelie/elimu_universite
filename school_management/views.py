from rest_framework import viewsets, views, response, status
from school_management.models import AcademicYear, Career, Document, DocumentType, GroupSubject, Level, Program, SanctionAppreciation, SanctionAppreciationType, Schedule, Sector, Semester, StudentCareer, Subject
from school_management.serializers import AcademicYearSerializer, CareerSerializer, DocumentSerializer, DocumentTypeSerializer, GroupSubjectSerializer, LevelSerializer, ProgramSerializer, SanctionAppreciationSerializer, SanctionAppreciationTypeSerializer, ScheduleSerializer, SectorSerializer, SemesterSerializer, StudentCareerSerializer, SubjectSerializer
from django.shortcuts import get_object_or_404, render
from.models import *
from django.http import JsonResponse


# Create your views here.
class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class SanctionAppreciationTypeViewSet(viewsets.ModelViewSet):
    queryset = SanctionAppreciationType.objects.all()
    serializer_class = SanctionAppreciationTypeSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class GroupSubjectViewSet(viewsets.ModelViewSet):
    queryset = GroupSubject.objects.all()
    serializer_class = GroupSubjectSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class StudentCareerViewSet(viewsets.ModelViewSet):
    queryset = StudentCareer.objects.all()
    serializer_class = StudentCareerSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class SanctionAppreciationViewSet(viewsets.ModelViewSet):
    queryset = SanctionAppreciation.objects.all()
    serializer_class = SanctionAppreciationSerializer


class TeacherScheduleListView(views.APIView):

    def get(self, request, format=None):
        teacher_id = request.data['teacher_id']
        print(teacher_id)
        schedules = Schedule.objects.filter(subject__teacher_in_charge=teacher_id)
        serializer = ScheduleSerializer(data=schedules, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


def teacher_schedule(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    subjects_taught = teacher.subject_set.all()
    
    schedules = Schedule.objects.filter(subject__in=subjects_taught)
    
    context = {'teacher': teacher, 'schedules': schedules}
    
    return render(request, 'teacher_schedule.html', context)


def teacher_documents(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    documents = Document.objects.filter(subject__teacher_in_charge=teacher)
    
    context = {'teacher': teacher, 'documents': documents}
    
    return render(request, 'teacher_documents.html', context)


def total_sanctions(request):
    total_sanctions_count = SanctionAppreciation.objects.count()
    
    return JsonResponse({'total_sanctions_count': total_sanctions_count})



def all_career_schedules(request):
    careers = Career.objects.all()
    
    schedules_by_career = {}
    for career in careers:
        schedules = Schedule.objects.filter(career=career)
        schedules_by_career[career] = schedules
    
    context = {'schedules_by_career': schedules_by_career}
    
    return render(request, 'all_career_schedules.html', context)


def students_and_careers(request, academic_year_id):
    student_careers = StudentCareer.objects.filter(academic_year_id=academic_year_id)
    
    return JsonResponse({'student_careers': student_careers})