from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.gestion_ecole_forms import EtablishmentForm
from backend.models.gestion_ecole import Etablishment, Student, Teacher
from backend.models.user_account import User

# Create your views here.
class IndexView(View):
    template_name = "administration/index.html"
    
    def get(self, request, *args, **kwargs):
        count_user = User.objects.all().count()
        count_teacher = Teacher.objects.all().count()
        count_student = Student.objects.filter(is_valid=True, status=True).count()
        context = {
            'count_user':count_user,
            'count_teacher':count_teacher,
            'count_student':count_student
        }
        return render(request, template_name=self.template_name, context=context)


class SchoolsView(View):
    template_name = "administration/schools/schools.html"
    
    def get(self, request, *args, **kwargs):
        schools = Etablishment.objects.all()
        return render(request, template_name=self.template_name, context={'schools':schools})
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Etablishment, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})


class AddSchoolView(View):
    template_name = "administration/schools/ajout_school.html"
    
    def get(self, request, *args, **kwargs):
        form = EtablishmentForm()
        return render(request, template_name=self.template_name, context={'form':form})
    
    def post(self, request, *args, **kwargs):
        form = EtablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:schools')
        return render(request, template_name=self.template_name, context={'form':form})