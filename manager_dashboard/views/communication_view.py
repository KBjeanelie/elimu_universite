from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.communication_forms import EventForm, GroupForm, InformationForm

from backend.models.communication import Event, Group, Information

class EditInformationView(View):
    template = "manager_dashboard/communication/editer_information.html"
    
    def get(self, request, pk, *args, **kwargs):
        info = get_object_or_404(Information, pk=pk)
        form = InformationForm(instance=info)
        context = {'form':form, 'info':info}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        info = get_object_or_404(Information, pk=pk)
        old_date = info.date_info
        
        mutable_data = request.POST.copy()
        mutable_files = request.FILES.copy()
    
        if 'file' not in mutable_files or not mutable_files['file']:
            mutable_files['file'] = None
            
        if 'date_info' not in request.POST or not request.POST['date_info']:
            mutable_data['date_info'] = old_date
            
        form = InformationForm(mutable_data, mutable_files, instance=info)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:informations')  # Redirigez vers la page appropriée après la mise à jour réussie
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'info': info}
        return render(request, template_name=self.template, context=context)

class AddInformationView(View):
    template = "manager_dashboard/communication/ajouter_information.html"
    form = InformationForm()
    context = {'form':form}
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context)


class InformationView(View):
    template = "manager_dashboard/communication/informations.html"
    def get(self, request, *args, **kwargs):
        context = {'informations': Information.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'informations': Information.objects.all().order_by('-created_at')}
            return render(request, template_name=self.template, context=context)
        
        context = {'informations': Information.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Information,pk=pk)
        instance.delete()
        context = {'informations': Information.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)


class InformationDetail(View):
    template = "manager_dashboard/communication/information_detail.html"
    
    def get(self, request, pk, *args, **kwargs):
        info = get_object_or_404(Information, pk=pk)
        object = {'info':info}
        return render(request, template_name=self.template, context=object)



class AddEventView(View):
    template = "manager_dashboard/communication/ajouter_evenement.html"
    form = EventForm()
    context = {'form':form}
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context)


class EditEventView(View):
    template = "manager_dashboard/communication/editer_evenement.html"
    def get(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        form = EventForm(instance=event)
        context = {'form':form, 'event':event}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        old_date1 = event.start_date
        old_date2 = event.end_date
        
        mutable_data = request.POST.copy()
        mutable_files = request.FILES.copy()
    
        if 'file' not in mutable_files or not mutable_files['file']:
            mutable_files['file'] = None
        if 'photo' not in mutable_files or not mutable_files['photo']:
            mutable_files['photo'] = None

        if 'start_date' not in request.POST or not request.POST['start_date']:
            mutable_data['start_date'] = old_date1
        if 'end_date' not in request.POST or not request.POST['end_date']:
            mutable_data['end_date'] = old_date2
            
        form = EventForm(mutable_data, mutable_files, instance=event)
        
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:events')
        
        context = {'form':form, 'event':event}
        return render(request, template_name=self.template, context=context)

class EventView(View):
    template = "manager_dashboard/communication/evenements.html"
    
    def get(self, request, *args, **kwargs):
        context = {'events': Event.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'events': Event.objects.all().order_by('-created_at')}
            return render(request, template_name=self.template, context=context)
        
        context = {'events': Event.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Event,pk=pk)
        instance.delete()
        context = {'events': Event.objects.all().order_by('-created_at')}
        return render(request, template_name=self.template, context=context)


class EventDetail(View):
    template = "manager_dashboard/communication/evenement_detail.html"
    
    def get(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        object = {'event':event}
        return render(request, template_name=self.template, context=object)


class GroupDiscussionView(View):
    template = "manager_dashboard/communication/group-discussions.html"
    form = GroupForm()
    
    def get(self, request, *args, **kwargs):
        groups = Group.objects.all().order_by('-created_at')
        contexte_object = {'group_discussions': groups, 'form':self.form}
        return render(request, template_name=self.template, context=contexte_object)
    
    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            groups = Group.objects.all().order_by('-created_at')
            contexte_object = {'group_discussions': groups, 'form':self.form}
            return render(request, template_name=self.template, context=contexte_object)
        
        return render(request, template_name=self.template, context=self.contexte_object)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Group, pk=pk)
        instance.delete()
        
        groups = Group.objects.all().order_by('-created_at')
        contexte_object = {'group_discussions': groups, 'form':self.form}
        return render(request, template_name=self.template, context=contexte_object)


