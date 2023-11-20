from rest_framework import serializers

from module_assessments.models import *

class TypeOfEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfEvaluation
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'



class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = '__all__'

        