from django.shortcuts import render
from django.views import View


class InformationsView(View):
    template_name = "accountant_dashboard/communication/informations.html"
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)