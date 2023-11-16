from rest_framework import viewsets
from school_management.models import AcademicYear, Career, Document, DocumentType, GroupSubject, Level, Program, SanctionAppreciation, SanctionAppreciationType, Schedule, Sector, Semester, StudentCareer, Subject
from school_management.serializers import AcademicYearSerializer, CareerSerializer, DocumentSerializer, DocumentTypeSerializer, GroupSubjectSerializer, LevelSerializer, ProgramSerializer, SanctionAppreciationSerializer, SanctionAppreciationTypeSerializer, ScheduleSerializer, SectorSerializer, SemesterSerializer, StudentCareerSerializer, SubjectSerializer

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
