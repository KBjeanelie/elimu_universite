from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from module_assessments.forms import AssessmentForm
from module_assessments.models import Assessment
from school_management.models import AcademicYear, Career, Semester, Subject
from django.db.models import Sum


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


class NoteTableView(View):
    template = 'manager_dashboard/evaluations/tableau_notes.html'
    
    semesters = Semester.objects.all().order_by('-created_at')
    careers = Career.objects.all().order_by('-created_at')
    subjects = Subject.objects.all().order_by('-created_at')
    
    def get(self, request, *args, **kwargs):
        semesters = Semester.objects.all().order_by('-created_at')
        careers = Career.objects.all().order_by('-created_at')
        subjects = Subject.objects.all().order_by('-created_at')
        context = {
            'semesters':semesters,
            'careers':careers,
            'subjects':subjects
        }
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        semester_id = request.POST['semester']
        career_id = request.POST['career']
        subject_id = request.POST['subject']
        
        try:
            semester = Semester.objects.get(pk=semester_id)
            career = Career.objects.get(pk=career_id)
            subject = Subject.objects.get(pk=subject_id)

            evaluations = Assessment.objects.filter(semester=semester, career=career, subject=subject).order_by('-note')

            if evaluations.exists():
                max_note = evaluations.first().note
                last_note = evaluations.last().note
                count = evaluations.count()
                sum_notes = evaluations.aggregate(total=Sum('note'))['total']
                average = sum_notes / count if count > 0 else 0

                
                context = {
                    'semesters':self.semesters,
                    'careers':self.careers,
                    'subjects':self.subjects,
                    'evaluations':evaluations,
                    'max_note':max_note,
                    'last_note':last_note,
                    'average':average
                }
                return render(request, template_name=self.template, context=context)
            else:
                context = {
                    'semesters':self.semesters,
                    'careers':self.careers,
                    'subjects':self.subjects,
                }
                return render(request, template_name=self.template, context=context)

        except (Semester.DoesNotExist, Career.DoesNotExist, Subject.DoesNotExist) as e:
            return HttpResponse(f"Erreur: {e}")

    
class AverageTableView(View):
    template = 'manager_dashboard/evaluations/tableau_moyennes.html'
    semesters = Semester.objects.all()
    careers = Career.objects.all()
    subjects = Subject.objects.all()
    
    def get(self, request, *args, **kwargs):
        context = {
            'semesters':self.semesters,
            'careers':self.careers,
            'subjects':self.subjects
        }
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        semester_id = request.POST['semester']
        career_id = request.POST['career']
        subject_id = request.POST['subject']
        
        try:
            semester = Semester.objects.get(pk=semester_id)
            career = Career.objects.get(pk=career_id)
            subject = Subject.objects.get(pk=subject_id)

            evaluations = Assessment.objects.filter(semester=semester, career=career, subject=subject).order_by('-note')

            if evaluations.exists():
                results = []
                controle_evaluations = evaluations.filter(type_evaluation__title='Contrôle')

                for controle_evaluation in controle_evaluations:
                    partiel_evaluation = evaluations.filter(
                        student=controle_evaluation.student,
                        type_evaluation__title='Partiel'
                    ).first()

                    if partiel_evaluation:
                        results.append(
                            {
                                'nui': controle_evaluation.student.registration_number,
                                'lastname': controle_evaluation.student.lastname,
                                'firstname': controle_evaluation.student.firstname,
                                'controle': controle_evaluation.note,
                                'partiel': partiel_evaluation.note,
                                'total': (
                                    (controle_evaluation.note+partiel_evaluation.note)* controle_evaluation.subject.coefficient
                                    ) / 2
                            }
                        )
                results = sorted(results, key=lambda x: x['controle'] + x['partiel'], reverse=True)
                
                if results:
                    average= round(sum(x['total'] for x in results) / len(results), 3)
                
                context = {
                    'semesters': self.semesters,
                    'careers': self.careers,
                    'subjects': self.subjects,
                    'results': results,
                    'max':results[0]['total'],
                    'last':results[-1]['total'],
                    
                    'average':average
                }
                return render(request, template_name=self.template, context=context)
# ...

            else:
                context = {
                    'semesters':self.semesters,
                    'careers':self.careers,
                    'subjects':self.subjects,
                }
                return render(request, template_name=self.template, context=context)

        except (Semester.DoesNotExist, Career.DoesNotExist, Subject.DoesNotExist) as e:
            return HttpResponse(f"Erreur: {e}")

class BullettinView(View):
    template = 'manager_dashboard/evaluations/bulletins.html'
    
    def get(self, request, *args, **kwargs):
        evaluations = Assessment.objects.all().order_by('-created_at')
        context = {'evaluations': evaluations}
        return render(request, template_name=self.template)