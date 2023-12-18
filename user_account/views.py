from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from user_account.models import ManagementProfil, Student, Teacher, User
from user_account.serializers import ManagementProfilSerializer, ManagerUserSerializer, StudentSerializer, StudentUserSerializer, TeacherSerializer, TeacherUserSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginAPIView(APIView):

    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        
        return Response({"errors:":"Username or password incorrect !"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "Déconnexion réussie"}, status=status.HTTP_200_OK)
        
        return Response({"error": "Aucun utilisateur connecté"}, status=status.HTTP_400_BAD_REQUEST)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherAccountView(APIView):
    
    def get(self, request, format=None):
        
        teacher_accounts = User.objects.filter(is_teacher=True)
        serializer = TeacherUserSerializer(teacher_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        student = User.objects.get(teacher=request.data['teacher_id'])
        student.delete()
        return Response({"Message": "Teacher account deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, student_id, format=None):
    #     student = self.get_student(student_id)
    #     serializer = UserSerializer(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None):
        try:
            # Récupère le matricule de l'étudiant envoyé
            teacher_id = request.data['teacher_id']
            
            # Obtient l'objet de l'étudiant
            teacher = Teacher.objects.get(id=teacher_id)
            
            new_account = User.objects.create_teacher_user(
                username=request.data['username'],
                teacher=teacher,
                password=request.data['password']
            )

            if new_account is not None:
                return Response({'Messages':"Teacher account created successfully !"}, status=status.HTTP_201_CREATED)
            
            return Response({'errors' : "Could not create teacher user :("}, status=status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            error_message = str(e)
            return Response({'error': "Teacher account already exist"}, status=status.HTTP_400_BAD_REQUEST)



class ManagementProfilViewSet(viewsets.ModelViewSet):
    queryset = ManagementProfil.objects.all()
    serializer_class = ManagementProfilSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAccountView(APIView):
    
    def get(self, request, format=None):
        
        students_accounts = User.objects.filter(is_student=True)
        serializer = StudentUserSerializer(students_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        student = User.objects.get(student=request.data['student_id'])
        student.delete()
        return Response({"Message": "Student account deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, student_id, format=None):
    #     student = self.get_student(student_id)
    #     serializer = UserSerializer(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None):
        try:
            # Récupère le matricule de l'étudiant envoyé
            student_registration_number = request.data['student']
            
            # Obtient l'objet de l'étudiant
            student = Student.objects.get(registration_number=student_registration_number)
            
            new_account = User.objects.create_student_user(
                username=request.data['username'],
                student=student,
                password=request.data['password']
            )

            if new_account is not None:
                return Response({'Messages':"Student account created successfully !"}, status=status.HTTP_201_CREATED)
            
            return Response({'errors' : "Could not create student user :("}, status=status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            error_message = str(e)
            return Response({'error': "Student account already exist"}, status=status.HTTP_400_BAD_REQUEST)




class ManagerAccountView(APIView):
    
    def get(self, request, format=None):
        
        manager_accounts = User.objects.filter(is_manager=True)
        serializer = ManagerUserSerializer(manager_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        manager = User.objects.get(management_profil=request.data['manager_id'])
        manager.delete()
        manager = ManagementProfil.objects.get(id=request.data['manager_id'])
        manager.delete()
        return Response({"Message": "Manager account deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, student_id, format=None):
    #     student = self.get_student(student_id)
    #     serializer = UserSerializer(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None):
        try:
            # creation d'un profil
            manager = ManagementProfil.objects.create()
            
            new_account = User.objects.create_manager_user(
                username=request.data['username'],
                manager_profil=manager,
                password=request.data['password']
            )

            if new_account is not None:
                return Response({'Messages':"Manger account created successfully !"}, status=status.HTTP_201_CREATED)
            
            return Response({'errors' : "Could not create manager user :("}, status=status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            error_message = str(e)
            return Response({'error': "Manager account already exist"}, status=status.HTTP_400_BAD_REQUEST)


class AccountantAccountView(APIView):
    
    def get(self, request, format=None):
        accountant_accounts = User.objects.filter(is_accountant=True)
        serializer = ManagerUserSerializer(accountant_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        accountant = User.objects.get(management_profil=request.data['accountant_id'])
        accountant.delete()
        accountant = ManagementProfil.objects.get(id=request.data['accountant_id'])
        accountant.delete()
        return Response({"Message": "Manager account deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, student_id, format=None):
    #     student = self.get_student(student_id)
    #     serializer = UserSerializer(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None):
        try:
            # creation d'un profil
            accountant = ManagementProfil.objects.create()
            
            new_account = User.objects.create_accountant_user(
                username=request.data['username'],
                manager_profil=accountant,
                password=request.data['password']
            )

            if new_account is not None:
                return Response({'Messages':"Accountant account created successfully !"}, status=status.HTTP_201_CREATED)
            
            return Response({'errors' : "Could not create accountant user :("}, status=status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            error_message = str(e)
            return Response({'error': "Accountant account already exist"}, status=status.HTTP_400_BAD_REQUEST)



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAccountView(APIView):
    
    def get(self, request, format=None):
        
        students_accounts = User.objects.filter(is_student=True)
        serializer = StudentUserSerializer(students_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        student = User.objects.get(student=request.data['student_id'])
        student.delete()
        return Response({"Message": "Student account deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, student_id, format=None):
    #     student = self.get_student(student_id)
    #     serializer = UserSerializer(student, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None):
        try:
            # Récupère le matricule de l'étudiant envoyé
            student_registration_number = request.data['student']
            
            # Obtient l'objet de l'étudiant
            student = Student.objects.get(registration_number=student_registration_number)
            
            new_account = User.objects.create_student_user(
                username=request.data['username'],
                student=student,
                password=request.data['password']
            )

            if new_account is not None:
                return Response({'Messages':"Student account created successfully !"}, status=status.HTTP_201_CREATED)
            
            return Response({'errors' : "Could not create student user :("}, status=status.HTTP_400_BAD_REQUEST)
        
        except IntegrityError as e:
            error_message = str(e)
            return Response({'error': "Student account already exist"}, status=status.HTTP_400_BAD_REQUEST)

