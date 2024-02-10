from django.shortcuts import render
from django.views import View
from manager_dashboard.views.gestion_evaluation_view import calculate_results, get_all_results

from school_management.models import AcademicYear, Career, Semester
from backend.models.user_account import Student


class ResultatAcademique(View):
    template_name = "manager_dashboard/statistique/resultat_academique.html"
    semesters = Semester.objects.all()
    careers = Career.objects.all()
    academic_year = AcademicYear.objects.get(status=True)
    total_student = Student.objects.all().count()
    results = get_all_results()
    admis, echouer = 0, 0
    
    for i in results:
        if i['average'] >= 10:
            admis += 1
        else:
            echouer += 1
            
    def get(self, request, *args, **kwargs):
        context = {
            'academic_year':self.academic_year, 
            'results':self.results, 
            'semesters':self.semesters, 
            'careers':self.careers,
            'total_student': self.total_student,
            'admis':self.admis,
            'echouer':self.echouer
        }
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        semester_id = request.POST['semester']
        career_id = request.POST['career']
        career = Career.objects.get(pk=career_id)
        semester = Semester.objects.get(pk=semester_id)
        results = calculate_results(semester_id=semester_id, career_id=career_id)
        if results:
            context = {
                'academic_year':self.academic_year, 
                'results':results, 
                'semesters':self.semesters, 
                'careers':self.careers,
                'total_student': self.total_student,
                'admis':self.admis,
                'echouer':self.echouer,
                'career':career,
                'semester':semester
            }
        else:
            context = {
                'academic_year':self.academic_year, 
                'semesters':self.semesters, 
                'careers':self.careers,
                'total_student': self.total_student,
                'admis':self.admis,
                'echouer':self.echouer
            }
            
        return render(request, template_name=self.template_name, context=context)