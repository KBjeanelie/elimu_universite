from rest_framework import viewsets
from module_assessments.models import TypeOfEvaluation
from module_assessments.serializers import TypeOfEvaluationSerializer

class TypeOfEvaluationViewSet(viewsets.ModelViewSet):
    queryset = TypeOfEvaluation.objects.all()
    serializer_class = TypeOfEvaluationSerializer
