from django.shortcuts import redirect, render
from django.views import View

class NotAcademicYearFound(View):
    template_name = "manager_dashboard/administration/no_academique.html"
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class ManagerIndexView(View):
    template_name = "manager_dashboard/index.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        if request.user.is_manager or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('backend:logout')
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)