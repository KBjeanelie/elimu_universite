from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from educational_content.forms import FileForm, FolderForm, eBookForm

from educational_content.models import File, Folder, eBook

class AddeBook(View):
    template = "manager_dashboard/contenue_pedagogique/ajout_ebook.html"
    form = eBookForm()
    context_object = {'form': form}
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)
    
    def post(self, request, *args, **kwargs):
        form = eBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:ebooks')
        
        return render(request, template_name=self.template, context=self.context_object)
    
class eBookView(View):
    template = 'manager_dashboard/contenue_pedagogique/ebooks.html'
    
    def get(self, request, *args, **kwargs):
        ebooks = eBook.objects.all().order_by('-created_at')
        context_object = {'ebooks': ebooks}
        return render(request, template_name=self.template, context=context_object)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(eBook, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})


class FolderViews(View):
    template = 'manager_dashboard/contenue_pedagogique/dossiers.html'
    folders = Folder.objects.all().order_by('-created_at')
    form = FolderForm()
    contexte_object = {'folders':folders, 'form':form}
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.contexte_object)
    
    def post(self, request, *args, **kwargs):
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard:folders')
        
        return render(request, template_name=self.template, context=self.contexte_object)


class FilesView(View):
    template = 'manager_dashboard/contenue_pedagogique/fichiers.html'
    
    def get(self, request, folder_id):
        folder = get_object_or_404(Folder, pk=folder_id)
        files = File.objects.filter(inFolder=folder)
        initial_data = {'inFolder': folder}
        form = FileForm(initial=initial_data)
        context_object = {'files': files, 'folder': folder, 'form':form}
        return render(request, template_name=self.template, context=context_object)
    
    def post(self, request, *args, **kwargs):
        form = FileForm(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            redirect('manager_dashboard:content_folder')
        
        return HttpResponse('Succès')
        
