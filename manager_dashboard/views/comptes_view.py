
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.user_account_forms import UserStudentForm, UserTeacherForm
from backend.models.user_account import User

#========================== PARTIE CONCERNANT LA GESTION DE COMPTE ENSEIGNANT
class EditTeacherAccountView(View):
    template = "manager_dashboard/comptes/editer_compte_enseignant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        print(user.password)
        form = UserTeacherForm(instance=user)
        context = {'form':form, 'account':user}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        form = UserTeacherForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_teacher = True
            user.save()
            return redirect('manager_dashboard:teachers_account')  # Redirigez vers la page appropriée après la mise à jour réussie
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'user': user}
        return render(request, template_name=self.template, context=context)
    
class AddTeacherAccount(View):
    template = "manager_dashboard/comptes/ajout_compte_enseignant.html"
    form = UserTeacherForm()
    context_object = {'form': form}
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)
    
    def post(self, request, *args, **kwargs):
        form = UserTeacherForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_teacher_user(
                form.cleaned_data['username'],
                form.cleaned_data['teacher'],
                form.cleaned_data['password'],
            )
        return redirect('manager_dashboard:teachers_account')

class ListAllTeacherAccount(View):
    template = "manager_dashboard/comptes/compte_enseignant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        teachers_account = User.objects.filter(is_teacher=True)
        context_object = {'teachers_account': teachers_account}
        return render(request, template_name=self.template, context=context_object)

    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(User, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})
#===END

#========================== PARTIE CONCERNANT LA GESTION DE COMPTE ETUDIANT
class EditStudentAccountView(View):
    template = "manager_dashboard/comptes/editer_compte_etudiant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        print(user.password)
        form = UserStudentForm(instance=user)
        context = {'form':form, 'account':user}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        form = UserStudentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_student = True
            user.save()
            return redirect('manager_dashboard:students_account')  # Redirigez vers la page appropriée après la mise à jour réussie
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'user': user}
        return render(request, template_name=self.template, context=context)

class AddStudentAccount(View):
    template = "manager_dashboard/comptes/ajout_compte_etudiant.html"
    form = UserStudentForm()
    context_object = {'form': form}
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)
    
    def post(self, request, *args, **kwargs):
        form = UserStudentForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_student_user(
                form.cleaned_data['username'],
                form.cleaned_data['student'],
                form.cleaned_data['password'],
            )
        return redirect('manager_dashboard:students_account')

class ListAllStudentAccount(View):
    template = "manager_dashboard/comptes/compte_etudiant.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        students_account = User.objects.filter(is_student=True)
        context_object = {'students_account': students_account}
        return render(request, template_name=self.template, context=context_object)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(User, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})