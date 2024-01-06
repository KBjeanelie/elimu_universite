from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from school_management.forms import SanctionAppreciationForm
from school_management.models import SanctionAppreciation

from user_account.models import Student, Teacher

class EditSanctionView(View):
    template = "manager_dashboard/gestion_universite/edit_sanction.html"
    def get(self, request, pk, *args, **kwargs):
        sanction = get_object_or_404(SanctionAppreciation, pk=pk)
        form = SanctionAppreciationForm(instance=sanction)
        context = {'form':form, 'sanction':sanction}
        return render(request, template_name=self.template, context=context)
    
class AddSanctionView(View):
    template = "manager_dashboard/gestion_universite/ajout_sanction.html"
    def get(self, request, *args, **kwargs):
        form = SanctionAppreciationForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = SanctionAppreciationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:sanction_appreciations")
        form = SanctionAppreciationForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class SanctionAppreciationView(View):
    template = "manager_dashboard/gestion_universite/sanctions.html"

    def get(self, request, *args, **kwargs):
        sanctions = SanctionAppreciation.objects.all().order_by('-created_at')
        context = {'sanctions':sanctions}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SanctionAppreciation, pk=pk)
        instance.delete()
        sanctions = SanctionAppreciation.objects.all().order_by('-created_at')
        context = {'sanctions':sanctions}
        return render(request, template_name=self.template, context=context)


class TrombinoscopeView(View):
    template = "manager_dashboard/gestion_universite/trombinoscopes.html"
    
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        context = {'students': students, 'teachers':teachers}
        return render(request, template_name=self.template, context=context)


class StudentDetailView(View):
    template = "manager_dashboard/gestion_universite/etudiant_detail.html"
    
    def get(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        context = {'student': student}
        return render(request, template_name=self.template, context=context)

class TeacherDetailView(View):
    template = "manager_dashboard/gestion_universite/enseignant_detail.html"
    
    def get(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        context = {'teacher':teacher}
        return render(request, template_name=self.template, context=context)