from rest_framework import serializers

from user_account.models import ManagementProfil, Student, Teacher, User, UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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