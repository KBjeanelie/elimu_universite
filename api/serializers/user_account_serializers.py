from rest_framework import serializers

from backend.models.user_account import User, Student, Teacher, ManagementProfil


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'management_profil', 'is_student', 'is_active','created_at', 'updated_at')


class ManagerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'student', 'is_manager', 'is_active','created_at', 'updated_at')

class TeacherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'teacher', 'is_teacher', 'is_active','created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', '')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ManagementProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementProfil
        fields = '__all__'