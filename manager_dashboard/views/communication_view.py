
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from module_communication.forms import GroupForm

from module_communication.models import Group


class InformationView(View):
    template = "manager_dashboard/communication/informations.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template)


class EventView(View):
    template = "manager_dashboard/communication/evenements.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template)


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


