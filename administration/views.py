from django.shortcuts import render
from django.views import View
from backend.models.gestion_ecole import Student, Teacher

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