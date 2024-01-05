
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from module_communication.forms import EventForm, GroupForm, InformationForm

from module_communication.models import Event, Group, Information

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


