from django.shortcuts import redirect, render
from django.views import View


class ManagerIndexView(View):
    template_name = "manager_dashboard/index.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)