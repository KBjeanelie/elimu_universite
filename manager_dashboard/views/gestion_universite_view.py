import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from manager_dashboard.views.gestion_evaluation_view import calculate_results
from backend.models.evaluations import Assessment
from backend.models.facturation import Invoice
from backend.forms.gestion_ecole_forms import AcademicYearForm, CareerForm, GroupSubjectForm, LevelForm, ProgramForm, SanctionAppreciationForm, SectorForm, SemesterForm, StudentDocumentForm, SubjectForm, TeacherDocumentForm
from backend.models.gestion_ecole import AcademicYear, Career, GroupSubject, Level, Program, SanctionAppreciation, Schedule, Sector, Semester, StudentCareer, StudentDocument, Subject, TeacherDocument
from backend.forms.user_account_forms import StudentForm, TeacherForm
from backend.models.user_account import Student, Teacher
from django.core.cache import cache
from django.db import transaction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def convertir_en_hexadecimal(nombre):
    # Utiliser la fonction hex() pour convertir le nombre en hexadécimal
    nombre_hexadecimal = hex(nombre)
    
    # La fonction hex() renvoie une chaîne qui commence par '0x', nous la supprimons
    nombre_hexadecimal = nombre_hexadecimal[2:]
    
    return nombre_hexadecimal

def generer_nui_etudiant():
    now = datetime.datetime.now()
    annee = now.year

    # Utilisation du cache pour stocker le compteur
    with transaction.atomic():
        student_counter = cache.get('student_counter') or 0
        student_counter += 1
        cache.set('student_counter', student_counter)

    identifiant_hexadecimal = convertir_en_hexadecimal(student_counter)
    return f"ELM-{annee}-STD-{identifiant_hexadecimal.upper()}"


#=============================== PARTIE CONCERNANT LES Année academique ==========================
class EditAcademicYearView(View):
    template = "manager_dashboard/gestion_universite/editer_annee_academique.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, pk, *args, **kwargs):
        academique_year = get_object_or_404(AcademicYear, pk=pk)
        form = AcademicYearForm(instance=academique_year)
        context = {'form':form, 'academique_year':academique_year}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        
        academique_year = get_object_or_404(AcademicYear, pk=pk, school=request.user.school)
        
        old_date1 = academique_year.start_date
        old_date2 = academique_year.end_date
        
        mutable_data = request.POST.copy()
        if 'start_date' not in request.POST or not request.POST['start_date']:
            mutable_data['start_date'] = old_date1
        if 'end_date' not in request.POST or not request.POST['end_date']:
            mutable_data['end_date'] = old_date2
        
        mutable_data['school'] = request.user.school
        
        form = AcademicYearForm(mutable_data, instance=academique_year)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:years')
        
        context = {'form':form, 'academique_year':academique_year}
        return render(request, template_name=self.template, context=context)
    
class AddAcademicYearView(View):
    template = "manager_dashboard/gestion_universite/ajout_annee_academique.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = AcademicYearForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = AcademicYearForm(data)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:years")
        form = AcademicYearForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class AcademicYearView(View):
    template = "manager_dashboard/gestion_universite/annee_academiques.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        academic_years = AcademicYear.objects.all().order_by('-label')
        context = {'academic_years': academic_years}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(AcademicYear, pk=pk)
        instance.delete()
        academic_years = AcademicYear.objects.all().order_by('-created_at')
        context = {'academic_years': academic_years}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES NIVEAUX ==========================
class LevelView(View):
    template = "manager_dashboard/gestion_universite/niveaux.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = LevelForm()
        context = {'levels':Level.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = LevelForm(data)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:levels')

        context = {'levels':Level.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Level, pk=pk)
        instance.delete()
        # redirection vers l'interface de vue des niveau
        form = LevelForm()
        context = {'levels':Level.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES SEMESTRE ==========================
class SemesterView(View):
    template = "manager_dashboard/gestion_universite/semestres.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = SemesterForm(request.user)
        context = {'semesters':Semester.objects.filter(level__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = SemesterForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='manager_dashboard:semesters')

        context = {'semesters':Semester.objects.filter(level__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Semester, pk=pk)
        instance.delete()
        
        form = SemesterForm(request.user)
        context = {'semesters':Semester.objects.filter(level__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES FILIÈRE ==========================
class SectorView(View):
    template = "manager_dashboard/gestion_universite/filieres.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = SectorForm()
        context = {'sectors':Sector.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = SectorForm(data)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:sectors')
    
        form = SectorForm()
        context = {'sectors':Sector.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Sector, pk=pk)
        instance.delete()
        
        form = SectorForm()
        context = {'sectors':Sector.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES PARCOURS ==========================
class CareerView(View):
    template = "manager_dashboard/gestion_universite/parcours.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = CareerForm(request.user)
        context = {'careers':Career.objects.filter(sector__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = CareerForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            redirect('manager_dashboard:careers')
    
        form = CareerForm(request.user)
        context = {'careers':Career.objects.filter(sector__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Career, pk=pk)
        instance.delete()
        
        form = CareerForm(request.user)
        context = {'careers':Career.objects.filter(sector__school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES GROUPES DE MATIÈRES ==========================
class GroupSubjectView(View):
    template = "manager_dashboard/gestion_universite/groupe_matieres.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = GroupSubjectForm()
        context = {'groups':GroupSubject.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = GroupSubjectForm(data)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:group_subjects')

        context = {'groups':GroupSubject.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(GroupSubject, pk=pk)
        instance.delete()
        
        form = GroupSubjectForm()
        context = {'groups':GroupSubject.objects.filter(school=request.user.school), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES MATIÈRES ==========================
class EditSubjectView(View):
    template = "manager_dashboard/gestion_universite/editer_matiere.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, pk, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(request.user, instance=subject)
        context = {'form':form, 'subject':subject}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(request.user, request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:subjects')  # Redirigez vers la page appropriée après la mise à jour réussie
        
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'subject': subject}
        return render(request, template_name=self.template, context=context)
    
class AddSubjectView(View):
    template = "manager_dashboard/gestion_universite/ajout_matiere.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = SubjectForm(request.user)
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = SubjectForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:subjects")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class SubjectView(View):
    template = "manager_dashboard/gestion_universite/matieres.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(level__school=request.user.school)
        items_per_page = 10
        
        paginator = Paginator(subjects, items_per_page)
        
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
            
        context = {'subjects':data_page}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Subject, pk=pk)
        instance.delete()
        
        subjects = Subject.objects.filter(level__school=request.user.school)
        context = {'subject':subjects}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES PROGRAMMES ==========================
class EditProgramView(View):
    template = "manager_dashboard/gestion_universite/editer_programme.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, pk, *args, **kwargs):
        program = get_object_or_404(Program, pk=pk)
        form = ProgramForm(instance=program)
        context = {'form':form, 'program':program}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        program = get_object_or_404(Program, pk=pk)
        
        old_date = program.program_date
        
        mutable_data = request.POST.copy()
        mutable_files = request.FILES.copy()
        
        if 'file' not in mutable_files or not mutable_files['file']:
            mutable_files['file'] = None
            
        if 'program_date' not in request.POST or not request.POST['program_date']:
            mutable_data['program_date'] = old_date
            
        mutable_data['school'] = request.user.school
        form = ProgramForm(mutable_data, mutable_files, instance=program)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:programs')  
        
        context = {'form':form, 'program':program}
        return render(request, template_name=self.template, context=context)


class AddProgramView(View):
    template = "manager_dashboard/gestion_universite/ajout_programme.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        form = ProgramForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = ProgramForm(data)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:programs")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class ProgramView(View):
    template = "manager_dashboard/gestion_universite/programmes.html"

    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        programs = Program.objects.filter(school=request.user.school)
        context = {'programs':programs}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Program, pk=pk)
        instance.delete()
        programs = Program.objects.filter(school=request.user.school)
        context = {'programs':programs}
        return render(request, template_name=self.template, context=context)
#===END

#================================= PARTIE CONCERNANT LES SANCTIONS ====================
class EditSanctionView(View):
    template = "manager_dashboard/gestion_universite/edit_sanction.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, pk, *args, **kwargs):
        sanction = get_object_or_404(SanctionAppreciation, pk=pk)
        form = SanctionAppreciationForm(request.user, instance=sanction)
        context = {'form':form, 'sanction':sanction}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        sanction = get_object_or_404(SanctionAppreciation, pk=pk)
        old_date = sanction.sanction_date
        
        mutable_data = request.POST.copy()
        if 'sanction_date' not in request.POST or not request.POST['sanction_date']:
            mutable_data['sanction_date'] = old_date
        
        mutable_data['school'] = request.user.school
        mutable_data['academic_year'] = AcademicYear.objects.get(status=True, school=request.user.school)
        form = SanctionAppreciationForm(request.user, mutable_data, instance=sanction)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:sanction_appreciations')  # Redirigez vers la page appropriée après la mise à jour réussie
        
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form':form, 'sanction':sanction}
        return render(request, template_name=self.template, context=context)
    
class AddSanctionView(View):
    template = "manager_dashboard/gestion_universite/ajout_sanction.html"
    
    def get(self, request, *args, **kwargs):
        form = SanctionAppreciationForm(request.user)
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        data['academic_year'] = AcademicYear.objects.get(status=True, school=request.user.school)
        form = SanctionAppreciationForm(request.user, data)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:sanction_appreciations")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class SanctionAppreciationView(View):
    template = "manager_dashboard/gestion_universite/sanctions.html"

    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        sanctions = SanctionAppreciation.objects.filter(academic_year__school=request.user.school, academic_year__status=True)
        context = {'sanctions':sanctions}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SanctionAppreciation, pk=pk)
        instance.delete()
        sanctions = SanctionAppreciation.objects.filter(school=request.user.school)
        context = {'sanctions':sanctions}
        return render(request, template_name=self.template, context=context)


class TrombinoscopeView(View):
    template = "manager_dashboard/gestion_universite/trombinoscopes.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        context = {'students': students, 'teachers':teachers}
        return render(request, template_name=self.template, context=context)


#=============================== PARTIE CONCERNANT LES Année academique ==========================
class EditTeacherView(View):
    template = "manager_dashboard/gestion_universite/editer_enseignant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(instance=teacher)
        context = {'form':form, 'teacher': teacher}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        bithday = teacher.bithday
        start_of_contrat = teacher.start_of_contrat
        end_of_contrat = teacher.end_of_contrat
        
        mutable_data = request.POST.copy()
        mutable_files = request.FILES.copy()
        
        if 'picture' not in mutable_files or not mutable_files['picture']:
            mutable_files['picture'] = None
        
        if 'bithday' not in request.POST or not request.POST['bithday']:
            mutable_data['bithday'] = bithday
        if 'start_of_contrat' not in request.POST or not request.POST['start_of_contrat']:
            mutable_data['start_of_contrat'] = start_of_contrat
        if 'end_of_contrat' not in request.POST or not request.POST['end_of_contrat']:
            mutable_data['end_of_contrat'] = end_of_contrat
        
        form = TeacherForm(mutable_data, mutable_files, instance=teacher)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:teachers')
        
        context = {'form':form, 'teacher': teacher}
        return render(request, template_name=self.template, context=context)
    
class AddTeacherView(View):
    template = "manager_dashboard/gestion_universite/ajout_enseignant.html"
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        form = TeacherForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:teachers")
        form = TeacherForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class TeacherView(View):
    template = "manager_dashboard/gestion_universite/enseignants.html"

    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all().order_by('-created_at')
        context = {'teachers': teachers}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Teacher, pk=pk)
        instance.delete()
        teachers = Teacher.objects.all().order_by('-created_at')
        context = {'teachers': teachers}
        return render(request, template_name=self.template, context=context)

class TeacherDetailView(View):
    template = "manager_dashboard/gestion_universite/enseignant_detail.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        subjects_taught_by_teacher = Subject.objects.filter(teacher_in_charge=teacher)
        schedules_for_subject = Schedule.objects.filter(subject__in=subjects_taught_by_teacher)
        documents = TeacherDocument.objects.filter(teacher=teacher)
        #account = get_object_or_404(User, teacher=teacher)
        form = TeacherDocumentForm()
        context = {'teacher':teacher, 'schedules_for_subject':schedules_for_subject, 'form':form, 'documents':documents}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request,pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        mutable_data = request.POST.copy()
        mutable_file = request.FILES.copy()
        mutable_data['teacher'] = teacher
        form = TeacherDocumentForm(mutable_data, mutable_file)
        if form.is_valid():
            form.save()
        
        subjects_taught_by_teacher = Subject.objects.filter(teacher_in_charge=teacher)
        schedules_for_subject = Schedule.objects.filter(subject__in=subjects_taught_by_teacher)
        documents = TeacherDocument.objects.filter(teacher=teacher)
        #account = get_object_or_404(User, teacher=teacher)
        form = TeacherDocumentForm()
        context = {'teacher':teacher, 'schedules_for_subject':schedules_for_subject, 'form':form, 'documents':documents}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        document = get_object_or_404(TeacherDocument, pk=pk)
        document.delete()
        return JsonResponse({'message': 'Document supprimé avec succès'})
#===END


#================================= PARTIE CONCERNANT LES ETUDIANT ======================
class EditStudentView(View):
    template = "manager_dashboard/gestion_universite/editer_etudiant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        context = {'form': StudentForm(instance=student), 'student':student}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        bithday = student.bithday
        
        mutable_data = request.POST.copy()
        mutable_files = request.FILES.copy()
        
        if 'picture' not in mutable_files or not mutable_files['picture']:
            mutable_files['picture'] = None
        
        if 'bithday' not in request.POST or not request.POST['bithday']:
            mutable_data['bithday'] = bithday
        
        form = StudentForm(mutable_data, mutable_files, instance=student)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:students')
        
        context = {'form':form, 'student': student}
        return render(request, template_name=self.template, context=context)


class AddStudentView(View):
    template = "manager_dashboard/gestion_universite/ajout_etudiant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        context = {'form': StudentForm()}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            registration_number = generer_nui_etudiant()
            lastname = form.data['lastname']
            firstname = form.data['firstname']
            bithday = form.data['bithday']
            tel = form.data['tel']
            sex = form.data['sex']
            new_student = Student(
                registration_number=registration_number,
                lastname=lastname,
                firstname=firstname,
                bithday=bithday,
                tel=tel,
                sex=sex
            )
            if 'status' in request.POST:
                new_student.status = True
                
            new_student.save()
            return redirect('manager_dashboard:students')
        else:
            print(form.errors)
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class StudentsView(View):

    template = "manager_dashboard/gestion_universite/etudiants.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, *args, **kwargs):
        try:
            academic_year = AcademicYear.objects.get(status=True, school=request.user.school)
            students = StudentCareer.objects.filter(academic_year=academic_year, is_registered=True, is_valid=False).order_by('-created_at')
            context = {'student_careers': students}
            return render(request, template_name=self.template, context=context)
        except AcademicYear.DoesNotExist:
            # Exécuter du code alternatif si l'objet AcademicYear n'existe pas
           return render(request, template_name=self.template)

class StudentDetailView(View):
    template = "manager_dashboard/gestion_universite/etudiant_detail.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')

    def get(self, request, pk, *args, **kwargs):
        academic_year = AcademicYear.objects.get(status=True, school=request.user.school)
        student = get_object_or_404(Student, pk=pk)
        documents = StudentDocument.objects.filter(student=student)
        sanctions_student = SanctionAppreciation.objects.filter(student=student)
        invoices_student = Invoice.objects.filter(student=student)
        controle_evaluations = Assessment.objects.filter(student=student, academic_year=academic_year, type_evaluation__title='Contrôle')
        partiel_evaluations = Assessment.objects.filter(student=student, academic_year=academic_year, type_evaluation__title='Partiel')
        students_career = StudentCareer.objects.filter(student=student)
        student_career = get_object_or_404(StudentCareer, student=student, academic_year=academic_year, is_valid=False)
        regulations = Invoice.objects.filter(school=request.user.school, invoice_status='Entièrement payé', student=student).order_by('-created_at')
        results = []
        monday_schedule = Schedule.objects.filter(career=student_career.career, day='lundi').order_by('start_hours')
        tueday_schedule = Schedule.objects.filter(career=student_career.career, day='mardi').order_by('start_hours')
        wednesday_schedule = Schedule.objects.filter(career=student_career.career, day='mercredi').order_by('start_hours')
        thursday_schedule = Schedule.objects.filter(career=student_career.career, day='jeudi').order_by('start_hours')
        friday_schedule = Schedule.objects.filter(career=student_career.career, day='vendredi').order_by('start_hours')
        saturday_schedule = Schedule.objects.filter(career=student_career.career, day='samedi').order_by('start_hours')
        
        for s in students_career:
            R = calculate_results(semester_id=s.semester.id, career_id=s.career.id, user=request.user)
            for r in R:
                if r['nui'] == student_career.student.registration_number:
                    results.append(r)

        form = StudentDocumentForm()
        context = {
            'student':student,
            'students_career':students_career,
            'student_career':student_career,
            'documents':documents,
            'sanctions_student':sanctions_student,
            'invoices_student':invoices_student,
            'controle_evaluations':controle_evaluations,
            'partiel_evaluations': partiel_evaluations,
            'form':form,
            'regulations':regulations,
            'results':results,
            'monday_schedule':monday_schedule,
            'tueday_schedule':tueday_schedule,
            'wednesday_schedule':wednesday_schedule,
            'thursday_schedule':thursday_schedule,
            'friday_schedule':friday_schedule,
            'saturday_schedule':saturday_schedule,
        }
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        mutable_data = request.POST.copy()
        mutable_file = request.FILES.copy()
        mutable_data['student'] = student
        form = StudentDocumentForm(mutable_data, mutable_file)
        if form.is_valid():
            form.save()
        
        academic_year = AcademicYear.objects.get(status=True)
        student = get_object_or_404(Student, pk=pk)
        documents = StudentDocument.objects.filter(student=student)
        sanctions_student = SanctionAppreciation.objects.filter(student=student)
        invoices_student = Invoice.objects.filter(student=student)
        controle_evaluations = Assessment.objects.filter(student=student, academic_year=academic_year, type_evaluation__title='Contrôle')
        partiel_evaluations = Assessment.objects.filter(student=student, academic_year=academic_year, type_evaluation__title='Partiel')
        student_carreer = get_object_or_404(StudentCareer, student=student)
        form = StudentDocumentForm()
        context = {
            'student':student,
            'student_career':student_carreer,
            'documents':documents,
            'sanctions_student':sanctions_student,
            'invoices_student':invoices_student,
            'controle_evaluations':controle_evaluations,
            'partiel_evaluations': partiel_evaluations,
            'form':form
        }
        return render(request, template_name=self.template, context=context)
    
    
    def delete(self, request, pk, *args, **kwargs):
        document = get_object_or_404(StudentDocument, pk=pk)
        document.delete()
        return JsonResponse({'message': 'Document supprimé avec succès'})
