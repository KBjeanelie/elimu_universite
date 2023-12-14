from requests import Response
from rest_framework import viewsets, status
from user_account.models import ManagementProfil, Student, Teacher, User, UserType
from user_account.serializers import ManagementProfilSerializer, StudentSerializer, TeacherSerializer, UserSerializer, UserTypeSerializer

# Create your views here.

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        # Récupère le mot de passe non haché depuis les données entrantes
        username = request.data.get('username')
        password = request.data.get('password')
        user_type = UserType.objects.get(pk = request.data.get('user_type'))

        new_user = User.objects.create_user(username, user_type, password,)

        serializer = self.get_serializer(new_user)
        return Response(serializer.data)
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ManagementProfilViewSet(viewsets.ModelViewSet):
    queryset = ManagementProfil.objects.all()
    serializer_class = ManagementProfilSerializer