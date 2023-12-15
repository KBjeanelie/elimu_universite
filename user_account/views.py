from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from user_account.models import ManagementProfil, Student, Teacher, User
from user_account.serializers import ManagementProfilSerializer, StudentSerializer, StudentUserSerializer, TeacherSerializer, TeacherUserSerializer, UserSerializer

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

