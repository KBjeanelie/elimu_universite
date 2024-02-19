from rest_framework import serializers
from backend.models.gestion_ecole import Student, Teacher
from backend.models.user_account import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
