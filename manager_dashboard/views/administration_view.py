from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from school_management.forms import DocumentTypeForm, SanctionAppreciationTypeForm
from school_management.models import DocumentType, SanctionAppreciationType
from user_account.forms import ManagementProfilForm

class TypeEvaluationView(View):
    template_name = "manager_dashboard/administration/type_evaluations.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class TypeDocumentView(View):
    template_name = "manager_dashboard/administration/type_documents.html"
    typeDocuments = DocumentType.objects.all().order_by('-created_at')
    context_object = {'type_documents': typeDocuments}
    
    def get(self, request, *args, **kwargs):
        type_documents = DocumentType.objects.all().order_by('-created_at')
        form = DocumentTypeForm()  # Formulaire pour la création
        context = {'type_documents': type_documents, 'form': form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = DocumentTypeForm(request.POST)  # Formulaire pour la création
        if form.is_valid():
            form.save()  # Sauvegarde du nouvel objet
            return redirect('manager_dashboard:type_documents')
        
        type_documents = DocumentType.objects.all().order_by('-created_at')
        context = {'type_documents': type_documents, 'form': form}
        return render(request, template_name=self.template_name, context=context)

    def put(self, request, *args, **kwargs):
        document_type_id = kwargs.get('id')
        instance = get_object_or_404(DocumentType, id=document_type_id)
        form = DocumentTypeForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()  # Sauvegarde de l'objet mis à jour
            return redirect('manager_dashboard:type_documents') 

class TypeDocumentDeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(DocumentType, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})

def get_last_document_type(request):
    last_object = DocumentType.objects.last()
    document_type = {
        'id': last_object.id,
        'title': last_object.title
    }
    
    return JsonResponse(document_type)



class TypeSanctionView(View):
    template_name = "manager_dashboard/administration/type_sanctions.html"
    typeSanctions = SanctionAppreciationType.objects.all().order_by('-created_at')
    context_object = {'type_sanctions': typeSanctions}
    
    def get(self, request, *args, **kwargs):
        typeSanctions = SanctionAppreciationType.objects.all().order_by('-created_at')
        form = SanctionAppreciationTypeForm()  # Formulaire pour la création
        context = {'type_sanctions': typeSanctions, 'form': form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = SanctionAppreciationTypeForm(request.POST)  # Formulaire pour la création
        if form.is_valid():
            form.save()  # Sauvegarde du nouvel objet
            return redirect('manager_dashboard:type_sanctions')
        
        typeSanctions = SanctionAppreciationType.objects.all().order_by('-created_at')
        context = {'type_sanctions': typeSanctions, 'form': form}
        return render(request, template_name=self.template_name, context=context)

    def put(self, request, *args, **kwargs):
        sanction_type_id = kwargs.get('id')
        instance = get_object_or_404(SanctionAppreciationType, id=sanction_type_id)
        form = SanctionAppreciationTypeForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()  # Sauvegarde de l'objet mis à jour
            return redirect('manager_dashboard:type_sanctions')


class TypeSanctionDeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SanctionAppreciationType, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})


def get_last_sanction_type(request):
    last_object = SanctionAppreciationType.objects.last()
    sanction_type = {
        'id': last_object.id,
        'title': last_object.title,
        'description': last_object.description
    }
    
    return JsonResponse(sanction_type)


class SettingAppView(View):
    template_name = "manager_dashboard/administration/reglage_generale.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
    
class ProfileAppView(View):
    template_name = "manager_dashboard/administration/profil.html"


    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('user_account:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = ManagementProfilForm()
        context = {'form':form}
        return render(request, template_name=self.template_name, context=context)