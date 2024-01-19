

from django.shortcuts import render
from django.views import View
from module_assessments.forms import AssessmentForm

from module_assessments.models import Assessment

class AddAssessmentView(View):
    template = 'manager_dashboard/evaluations/ajout_evaluation.html'
    
    def get(self, request, *args, **kwargs):
        form = AssessmentForm()
        context = {'form': form}
        return render(request, template_name=self.template, context=context)

class AssessmentView(View):
    template = 'manager_dashboard/evaluations/evaluations.html'
    
    def get(self, request, *args, **kwargs):
        evaluations = Assessment.objects.all()
        context = {'evaluations': evaluations}
        return render(request, template_name=self.template, context=context)