from rest_framework import viewsets
from user_account.models import ManagementProfil, Student, Teacher, User, UserType
from user_account.serializers import ManagementProfilSerializer, StudentSerializer, TeacherSerializer, UserSerializer, UserTypeSerializer

# Create your views here.

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ManagementProfilViewSet(viewsets.ModelViewSet):
    queryset = ManagementProfil.objects.all()
    serializer_class = ManagementProfilSerializer