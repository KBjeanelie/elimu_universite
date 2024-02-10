from django.shortcuts import render
from django.views import View

from backend.models.communication import Event, Information


class InformationsView(View):
    template_name = "accountant_dashboard/communication/informations.html"
    
    def get(self, request, *args, **kwargs):
        object = {'informations': Information.objects.filter(status=True)}
        return render(request, template_name=self.template_name, context=object)

class EventsView(View):
    template_name = "accountant_dashboard/communication/evenements.html"
    
    def get(self, request, *args, **kwargs):
        object = {'events': Event.objects.filter(status=True)}
        return render(request, template_name=self.template_name, context=object)