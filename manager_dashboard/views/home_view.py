from django.shortcuts import render
from django.views import View


class ManagerIndexView(View):
    template_name = "manager_dashboard/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)