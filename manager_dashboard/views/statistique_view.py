from django.shortcuts import render
from django.views import View
from manager_dashboard.views.gestion_evaluation_view import calculate_results, get_all_results
from backend.models.gestion_ecole import AcademicYear, Career, Semester, StudentCareer
from django.http import Http404

class ResultatAcademique(View):
    template_name = "manager_dashboard/statistique/resultat_academique.html"
    
    def get_context_data(self, request, **kwargs):
        semesters = Semester.objects.filter(level__school=self.request.user.school)
        careers = Career.objects.filter(sector__school=self.request.user.school)
        academic_year = AcademicYear.objects.filter(status=True, school=self.request.user.school).first()
        total_student = StudentCareer.objects.filter(academic_year=academic_year).count()
        results = get_all_results(request.user)
        admis, echouer = 0, 0
        
        for i in results:
            if i['average'] >= 10:
                admis += 1
            else:
                echouer += 1
        context = {
            'academic_year': academic_year, 
            'results': results, 
            'semesters': semesters, 
            'careers': careers,
            'total_student': total_student,
            'admis': admis,
            'echouer': echouer
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        semester_id = request.POST.get('semester')
        career_id = request.POST.get('career')
        try:
            career = Career.objects.get(pk=career_id)
            semester = Semester.objects.get(pk=semester_id)
        except (Career.DoesNotExist, Semester.DoesNotExist):
            raise Http404("Selected semester or career does not exist.")
        
        context = self.get_context_data(request)
        results = calculate_results(semester_id=semester_id, career_id=career_id, user=request.user)
        
        context.update({
            'career': career,
            'semester': semester,
            'results':results
        })
        return render(request, template_name=self.template_name, context=context)
