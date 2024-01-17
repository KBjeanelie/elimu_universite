from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from school_management.forms import AcademicYearForm, CareerForm, GroupSubjectForm, LevelForm, ProgramForm, SanctionAppreciationForm, SectorForm, SemesterForm, SubjectForm
from school_management.models import AcademicYear, Career, GroupSubject, Level, Program, SanctionAppreciation, Sector, Semester, Subject
from user_account.forms import TeacherForm

from user_account.models import Student, Teacher, User

#=============================== PARTIE CONCERNANT LES Année academique ==========================
class EditAcademicYearView(View):
    template = "manager_dashboard/gestion_universite/edit_sanction.html"
    def get(self, request, pk, *args, **kwargs):
        academique_year = get_object_or_404(AcademicYear, pk=pk)
        form = AcademicYearForm(instance=academique_year)
        context = {'form':form, 'academique_year':academique_year}
        return render(request, template_name=self.template, context=context)
    
class AddAcademicYearView(View):
    template = "manager_dashboard/gestion_universite/ajout_annee_academique.html"
    def get(self, request, *args, **kwargs):
        form = AcademicYearForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:years")
        form = AcademicYearForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class AcademicYearView(View):
    template = "manager_dashboard/gestion_universite/annee_academiques.html"

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
    
    def get(self, request, *args, **kwargs):
        form = LevelForm()
        context = {'levels':Level.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            form = LevelForm()
            context = {'levels':Level.objects.all().order_by('-created_at'), 'form':form}
            return render(request, template_name=self.template, context=context)
    
        form = LevelForm()
        context = {'levels':Level.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Level, pk=pk)
        instance.delete()
        form = LevelForm()
        context = {'levels':Level.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES SEMESTRE ==========================
class SemesterView(View):
    template = "manager_dashboard/gestion_universite/semestres.html"
    
    def get(self, request, *args, **kwargs):
        form = SemesterForm()
        context = {'semesters':Semester.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            form = SemesterForm()
            context = {'semesters':Semester.objects.all().order_by('-created_at'), 'form':form}
            return render(request, template_name=self.template, context=context)
    
        form = SemesterForm()
        context = {'semesters':Semester.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Semester, pk=pk)
        instance.delete()
        form = SemesterForm()
        context = {'semesters':Semester.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES FILIÈRE ==========================
class SectorView(View):
    template = "manager_dashboard/gestion_universite/filieres.html"
    
    def get(self, request, *args, **kwargs):
        form = SectorForm()
        context = {'sectors':Sector.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = SectorForm(request.POST)
        if form.is_valid():
            form.save()
            form = SectorForm()
            context = {'sectors':Sector.objects.all().order_by('-created_at'), 'form':form}
            return render(request, template_name=self.template, context=context)
    
        form = SectorForm()
        context = {'sectors':Sector.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Sector, pk=pk)
        instance.delete()
        form = SectorForm()
        context = {'sectors':Sector.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES PARCOURS ==========================
class CareerView(View):
    template = "manager_dashboard/gestion_universite/parcours.html"
    
    def get(self, request, *args, **kwargs):
        form = CareerForm()
        context = {'careers':Career.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CareerForm()
            context = {'careers':Career.objects.all().order_by('-created_at'), 'form':form}
            return render(request, template_name=self.template, context=context)
    
        form = CareerForm()
        context = {'careers':Career.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Career, pk=pk)
        instance.delete()
        form = CareerForm()
        context = {'careers':Career.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES GROUPES DE MATIÈRES ==========================
class GroupSubjectView(View):
    template = "manager_dashboard/gestion_universite/groupe_matieres.html"
    
    def get(self, request, *args, **kwargs):
        form = GroupSubjectForm()
        context = {'groups':GroupSubject.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)

    def post(self, request, *args, **kwargs):
        form = GroupSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            form = GroupSubjectForm()
            context = {'groups':GroupSubject.objects.all().order_by('-created_at'), 'form':form}
            return render(request, template_name=self.template, context=context)
    
        form = GroupSubjectForm()
        context = {'groups':GroupSubject.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(GroupSubject, pk=pk)
        instance.delete()
        form = GroupSubjectForm()
        context = {'groups':GroupSubject.objects.all().order_by('-created_at'), 'form':form}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES MATIÈRES ==========================
class EditSubjectView(View):
    template = "manager_dashboard/gestion_universite/editer_matiere.html"
    def get(self, request, pk, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(instance=subject)
        context = {'form':form, 'subject':subject}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=pk)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:subjects')  # Redirigez vers la page appropriée après la mise à jour réussie
        
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'subject': subject}
        return render(request, template_name=self.template, context=context)
    
class AddSubjectView(View):
    template = "manager_dashboard/gestion_universite/ajout_matiere.html"
    def get(self, request, *args, **kwargs):
        form = SubjectForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:subjects")
        form = SubjectForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class SubjectView(View):
    template = "manager_dashboard/gestion_universite/matieres.html"

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all().order_by('-created_at')
        context = {'subjects':subjects}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Subject, pk=pk)
        instance.delete()
        subjects = Subject.objects.all().order_by('-created_at')
        context = {'subject':subjects}
        return render(request, template_name=self.template, context=context)
#===END

#=============================== PARTIE CONCERNANT LES PROGRAMMES ==========================
class EditProgramView(View):
    template = "manager_dashboard/gestion_universite/edit_sanction.html"
    def get(self, request, pk, *args, **kwargs):
        program = get_object_or_404(Program, pk=pk)
        form = ProgramForm(instance=program)
        context = {'form':form, 'program':program}
        return render(request, template_name=self.template, context=context)
    
class AddProgramView(View):
    template = "manager_dashboard/gestion_universite/ajout_programme.html"
    def get(self, request, *args, **kwargs):
        form = ProgramForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard:programs")
        form = ProgramForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class ProgramView(View):
    template = "manager_dashboard/gestion_universite/programmes.html"

    def get(self, request, *args, **kwargs):
        programs = Program.objects.all().order_by('-created_at')
        context = {'programs':programs}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Program, pk=pk)
        instance.delete()
        programs = Program.objects.all().order_by('-created_at')
        context = {'programs':programs}
        return render(request, template_name=self.template, context=context)
#===END

#================================= PARTIE CONCERNANT LES SANCTIONS ====================
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



#=============================== PARTIE CONCERNANT LES Année academique ==========================
class EditTeacherView(View):
    template = "manager_dashboard/gestion_universite/edit_sanction.html"
    def get(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(instance=teacher)
        context = {'form':form, 'teacher': teacher}
        return render(request, template_name=self.template, context=context)
    
class AddTeacherView(View):
    template = "manager_dashboard/gestion_universite/ajout_enseignant.html"
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
    
    def get(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        account = get_object_or_404(User, teacher=teacher)
        context = {'teacher':teacher, 'account': account}
        return render(request, template_name=self.template, context=context)
#===END