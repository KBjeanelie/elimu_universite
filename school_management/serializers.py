from rest_framework import serializers
from school_management.models import AcademicYear, Career, Document, DocumentType, GroupSubject, Level, Program, SanctionAppreciation, SanctionAppreciationType, Schedule, Sector, Semester, StudentCareer, Subject


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class SanctionAppreciationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionAppreciationType
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GroupSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSubject
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'


class StudentCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCareer
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class SanctionAppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionAppreciation
        fields = '__all__'