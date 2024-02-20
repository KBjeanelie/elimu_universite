from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from backend.forms.user_account_forms import LoginForm
from backend.models.gestion_ecole import AcademicYear


# Create your views here.
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('backend:login')


class LoginView(View):
    template_name = 'backend/login.html'
    context_object = {'form': LoginForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        sign_form = LoginForm(request.POST)
        username = sign_form['username'].value()
        password = sign_form['password'].value()
        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect(to='backend:login')
        login(request, user)
        
        years = AcademicYear.objects.filter(school=user.school)
        
        for academic_year in years:
            if academic_year.status:
                request.session['academic_year'] = academic_year.label
                break


        if user.is_manager or user.is_admin:
            return redirect(to='manager_dashboard:index')
        if user.is_accountant:
            return redirect(to='accountant_dashboard:index')