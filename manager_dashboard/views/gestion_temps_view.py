from django.shortcuts import redirect, render
from django.views import View

from backend.forms.gestion_ecole_forms import ScheduleForm
from school_management.models import Career, Schedule, Semester

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
    semesters = Semester.objects.all()
    careers = Career.objects.all()
    
    def get(self, request, *args, **kwargs):
        context = {
            'semesters':self.semesters,
            'careers':self.careers,
        }
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        #semester_id = request.POST['semester']
        career_id = request.POST['career']
        career = Career.objects.get(pk=career_id)
        
        monday_schedule = Schedule.objects.filter(career__id=career_id, day='lundi').order_by('start_hours')
        tueday_schedule = Schedule.objects.filter(career__id=career_id, day='mardi').order_by('start_hours')
        wednesday_schedule = Schedule.objects.filter(career__id=career_id, day='mercredi').order_by('start_hours')
        thursday_schedule = Schedule.objects.filter(career__id=career_id, day='jeudi').order_by('start_hours')
        friday_schedule = Schedule.objects.filter(career__id=career_id, day='vendredi').order_by('start_hours')
        saturday_schedule = Schedule.objects.filter(career__id=career_id, day='samedi').order_by('start_hours')
        
        context = {
            'semesters':self.semesters,
            'careers':self.careers,
            'monday_schedule':monday_schedule,
            'tueday_schedule':tueday_schedule,
            'wednesday_schedule':wednesday_schedule,
            'thursday_schedule':thursday_schedule,
            'friday_schedule':friday_schedule,
            'saturday_schedule':saturday_schedule,
            'career':career
        }
        return render(request, template_name=self.template, context=context)
        
        return super().post(request, *args, **kwargs)