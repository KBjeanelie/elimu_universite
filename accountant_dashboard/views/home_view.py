from django.shortcuts import render
from django.views import View


class AccountantIndexView(View):
    template_name = "accountant_dashboard/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)