from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.evaluation_forms import AssessmentForm
from backend.models.evaluations import Assessment
from backend.models.gestion_ecole import AcademicYear, Career, Semester, StudentCareer, Subject
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def calculate_results(semester_id, career_id):
    academic_year = AcademicYear.objects.get(status=True)
    
    try:
        semester = Semester.objects.get(pk=semester_id)
        career = Career.objects.get(pk=career_id)

        evaluations = Assessment.objects.filter(semester=semester, career=career, academic_year=academic_year).order_by('-note')
        student_career = StudentCareer.objects.filter(semester=semester, career=career, academic_year=academic_year)
    
        if evaluations.exists():
            results = []
            controle_evaluations = evaluations.filter(type_evaluation__title='Contrôle')
            partiel_evaluations = evaluations.filter(type_evaluation__title='Partiel')

            for student in student_career:
                m = []
                count_coefficient = 0

                for controle_evaluation in controle_evaluations.filter(student=student.student):
                    count_coefficient += controle_evaluation.subject.coefficient
                    partiel_evaluation = partiel_evaluations.filter(
                        student=controle_evaluation.student,
                        subject=controle_evaluation.subject
                    ).first()

                    if partiel_evaluation:
                        total = ((controle_evaluation.note + partiel_evaluation.note) * controle_evaluation.subject.coefficient) / 2
                        m.append(
                            {
                                'id_student':student.id,
                                'nui': controle_evaluation.student.registration_number,
                                'lastname': controle_evaluation.student.lastname,
                                'firstname': controle_evaluation.student.firstname,
                                'controle': controle_evaluation.note,
                                'partiel': partiel_evaluation.note,
                                'semestre':controle_evaluation.semester.title,
                                'niveau':controle_evaluation.semester.level.label,
                                'parcours':controle_evaluation.career.title,
                                'year':controle_evaluation.academic_year.label,
                                'total': total,
                            }
                        )

                if m:
                    # Calculer la moyenne pondérée
                    average = round(sum(x['total'] for x in m) / count_coefficient, 2) if count_coefficient != 0 else 0

                    results.append({
                        'id_student': m[0]['id_student'],
                        'nui': m[0]['nui'],
                        'lastname': m[0]['lastname'],
                        'firstname': m[0]['firstname'],
                        'semestre': m[0]['semestre'],
                        'niveau': m[0]['niveau'],
                        'parcours': m[0]['parcours'],
                        'year':m[0]['year'],
                        'average': average,
                    })

            # Tri des résultats par rapport à 'average'
            results = sorted(results, key=lambda x: x['average'], reverse=True)

            # Ajout du rang à chaque résultat
            for i, result in enumerate(results, start=1):
                result['rang'] = i

            return results

        else:
            return []

    except (Semester.DoesNotExist, Career.DoesNotExist, Subject.DoesNotExist) as e:
        return HttpResponse(f"Erreur: {e}")


def get_all_results():
    academic_year = AcademicYear.objects.get(status=True)
    semesters = Semester.objects.all()
    results = []
    
    for semester in semesters:
        try:
            evaluations = Assessment.objects.filter(academic_year=academic_year, semester=semester).order_by('semester__title')
            student_career = StudentCareer.objects.filter(academic_year=academic_year, is_valid=False, semester=semester)

            if evaluations.exists():
                controle_evaluations = evaluations.filter(type_evaluation__title='Contrôle')
                partiel_evaluations = evaluations.filter(type_evaluation__title='Partiel')

                for student in student_career:
                    m = []
                    count_coefficient = 0

                    for controle_evaluation in controle_evaluations.filter(student=student.student):
                        count_coefficient += controle_evaluation.subject.coefficient
                        partiel_evaluation = partiel_evaluations.filter(
                            student=controle_evaluation.student,
                            subject=controle_evaluation.subject
                        ).first()

                        if partiel_evaluation:
                            total = ((controle_evaluation.note + partiel_evaluation.note) * controle_evaluation.subject.coefficient) / 2
                            m.append(
                                {
                                    'id_student':student.id,
                                    'nui': controle_evaluation.student.registration_number,
                                    'lastname': controle_evaluation.student.lastname,
                                    'firstname': controle_evaluation.student.firstname,
                                    'controle': controle_evaluation.note,
                                    'partiel': partiel_evaluation.note,
                                    'semestre':controle_evaluation.semester.title,
                                    'niveau':controle_evaluation.semester.level.label,
                                    'parcours':controle_evaluation.career.title,
                                    'year':controle_evaluation.academic_year.label,
                                    'total': total,
                                }
                            )

                    if m:
                        # Calculer la moyenne pondérée
                        average = round(sum(x['total'] for x in m) / count_coefficient, 2) if count_coefficient != 0 else 0

                        results.append({
                            'id_student': m[0]['id_student'],
                            'nui': m[0]['nui'],
                            'lastname': m[0]['lastname'],
                            'firstname': m[0]['firstname'],
                            'semestre': m[0]['semestre'],
                            'niveau': m[0]['niveau'],
                            'parcours': m[0]['parcours'],
                            'year':m[0]['year'],
                            'average': average,
                        })

                # Tri des résultats par rapport à 'average'
                results = sorted(results, key=lambda x: x['average'], reverse=True)

                # Ajout du rang à chaque résultat
                for i, result in enumerate(results, start=1):
                    result['rang'] = i
                    
        except (Semester.DoesNotExist, Career.DoesNotExist, Subject.DoesNotExist) as e:
            return HttpResponse(f"Erreur: {e}")
        
    return results




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
        # Nombre d'éléments par page
        items_per_page = 10
        
        paginator = Paginator(evaluations, items_per_page)
        
        page = request.GET.get('page')
        
        try:
            # Obtenez les éléments de la page demandée
            data_page = paginator.page(page)
        except PageNotAnInteger:
            # Si la page n'est pas un entier, affichez la première page
            data_page = paginator.page(1)
        except EmptyPage:
            # Si la page est en dehors de la plage, affichez la dernière page
            data_page = paginator.page(paginator.num_pages)
            
        context = {'evaluations': data_page}
        
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
                    'max': results[0]['total'],
                    'last': results[-1]['total'],
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
    
    semesters = Semester.objects.all()
    careers = Career.objects.all()
    
    def get(self, request, *args, **kwargs):
        context = {
            'semesters':self.semesters,
            'careers':self.careers,
        }
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        semester_id = request.POST['semester']
        career_id = request.POST['career']
        
        
        
        results = calculate_results(semester_id=semester_id, career_id=career_id)

        if results:
            context = {
                'semesters': self.semesters,
                'careers': self.careers,
                'results': results,
            }
        else:
            context = {
                'semesters': self.semesters,
                'careers': self.careers,
            }

        return render(request, template_name=self.template, context=context)


class BulletinDetailView(View):
    template = 'manager_dashboard/evaluations/bulletin_detail.html'
    
    def get(self, request, pk, *args, **kwargs):
        academic_year = AcademicYear.objects.get(status=True)
        student_career = StudentCareer.objects.get(pk=pk, academic_year=academic_year)
        total_student = StudentCareer.objects.filter(semester=student_career.semester, career=student_career.career, academic_year=academic_year).count()
        evaluations = Assessment.objects.filter(semester=student_career.semester, career=student_career.career, academic_year=academic_year).order_by('subject__label')
        
        if evaluations.exists():

            controle_evaluations = evaluations.filter(type_evaluation__title='Contrôle')
            partiel_evaluations = evaluations.filter(type_evaluation__title='Partiel')

            subjects = []
            count_coefficient = 0

            for controle_evaluation in controle_evaluations.filter(student=student_career.student):
                count_coefficient += controle_evaluation.subject.coefficient
                partiel_evaluation = partiel_evaluations.filter(
                    student=controle_evaluation.student,
                    subject=controle_evaluation.subject
                ).first()

                if partiel_evaluation:
                    total = ((controle_evaluation.note + partiel_evaluation.note) * controle_evaluation.subject.coefficient) / 2
                    subjects.append(
                        {
                            'nui': controle_evaluation.student.registration_number,
                            'controle': controle_evaluation.note,
                            'partiel': partiel_evaluation.note,
                            'label':controle_evaluation.subject.label,
                            'coefficient':controle_evaluation.subject.coefficient,
                            'total': total,
                        }
                    )

            # Calculer la moyenne pondérée
            average = round(sum(x['total'] for x in subjects) / count_coefficient, 2) if count_coefficient != 0 else 0
            total_general = round(sum(x['total'] for x in subjects), 2)

            result = {
                'nui': subjects[0]['nui'],
                'average': average,
                'count_coefficient':count_coefficient,
                'total_general':total_general
            }

        context = {
            'student_career':student_career,
            'year':academic_year,
            'result': result,
            'subjects':subjects,
            'total_student':total_student
        }
        return render(request, template_name=self.template, context=context)