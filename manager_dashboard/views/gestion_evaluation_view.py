

from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from module_assessments.forms import AssessmentForm

from module_assessments.models import Assessment
from school_management.models import AcademicYear

class EditAssessmentView(View):
    template = 'manager_dashboard/evaluations/editer_evaluation.html'
    
    def get(self, request, pk, *args, **kwargs):
        evaluation = get_object_or_404(Assessment, pk=pk)
        form = AssessmentForm(instance=evaluation)
        context = {'form': form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        evaluation = get_object_or_404(Assessment, pk=pk)
        year = get_object_or_404(AcademicYear, status=True)
        mutable_data = request.POST.copy()
        mutable_data['academic_year'] = year
        form = AssessmentForm(mutable_data, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:evaluations')
        else:
            print(form.errors)
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class AddAssessmentView(View):
    template = 'manager_dashboard/evaluations/ajout_evaluation.html'
    
    def get(self, request, *args, **kwargs):
        form = AssessmentForm()
        context = {'form': form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        year = get_object_or_404(AcademicYear, status=True)
        mutable_data = request.POST.copy()
        mutable_data['academic_year'] = year
        form = AssessmentForm(mutable_data)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:evaluations')
        else:
            print(form.errors)
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
class AssessmentView(View):
    template = 'manager_dashboard/evaluations/evaluations.html'
    
    def get(self, request, *args, **kwargs):
        evaluations = Assessment.objects.all().order_by('-created_at')
        context = {'evaluations': evaluations}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Assessment, pk=pk)
        instance.delete()
        evaluations = Assessment.objects.all().order_by('-created_at')
        context = {'evaluations': evaluations}
        return render(request, template_name=self.template, context=context)