from django.shortcuts import redirect, render
from django.views import View

from school_management.forms import ScheduleForm

class AddScheduleView(View):
    template = 'manager_dashboard/gestion_temps/ajout_emplois_temps.html'
    
    def get(self, request, *args, **kwargs):
        form = ScheduleForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = ScheduleForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:times')
        
        form = ScheduleForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)


class ScheduleView(View):
    template = 'manager_dashboard/gestion_temps/emplois_temps.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template)