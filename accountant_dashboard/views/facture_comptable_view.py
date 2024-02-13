import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.facturation_forms import InvoiceForm, RegulationsForm
from backend.models.facturation import Invoice, Regulations
from django.core.cache import cache

def generate_payment_number():
        now = datetime.datetime.now()
        year = now.year
        # Utilisation du cache pour stocker le compteur
        regulation_counter = cache.get('regulation_counter') or 0
        regulation_counter += 1
        cache.set('regulation_counter', regulation_counter)

        return f"REGL{year}{regulation_counter}"
    
def generate_invoice_number():
        now = datetime.datetime.now()
        year = now.year
        # Utilisation du cache pour stocker le compteur
        invoice_counter = cache.get('invoice_counter') or 0
        invoice_counter += 1
        cache.set('invoice_counter', invoice_counter)
        
        return f"FA{year}{invoice_counter}"

class InvoiceView(View):
    template_name = "accountant_dashboard/facture_comp/factures.html"
    
    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.filter(school=request.user.school)
        form = InvoiceForm(request.user,)
        context = {'invoices':invoices, 'form':form}
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = InvoiceForm(request.user, request.POST)
        if form.is_valid():
            invoice_number = generate_invoice_number()
            career = form.cleaned_data['career']
            item = form.cleaned_data['item']
            student = form.cleaned_data['student']
            comment = form.cleaned_data['comment']
            invoice_status = form.cleaned_data['invoice_status']
            
            # Utilisation des valeurs récupérées pour créer une nouvelle instance de la facture
            invoice = Invoice(
                invoice_number=invoice_number,
                career=career,
                item=item,
                student=student,
                comment=comment,
                school=request.user.school,
                invoice_status=invoice_status
            )
            invoice.save()
            return redirect("accountant_dashboard:invoices")
        
        return redirect("accountant_dashboard:invoices")
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Invoice, pk=pk)
        instance.delete()
        invoices = Invoice.objects.all().order_by('-created_at')
        context = {'invoices':invoices}
        return render(request, template_name=self.template_name, context=context)

class InvoiceDetailView(View):
    template_name = "accountant_dashboard/facture_comp/facture-info.html"
    
    def get(self, request,pk, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=pk)
        regulation = get_object_or_404(Regulations, invoice=invoice)
        context = {'invoice':invoice, 'regulation':'regulation'}
        return render(request, template_name=self.template_name, context=context)

class EditInvoiceView(View):
    template_name = "accountant_dashboard/facture_comp/edit_facture.html"
    
    def get(self, request,pk, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=pk)
        form = InvoiceForm(request.user, instance=invoice)
        context = {'invoice':invoice, 'form':form}
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        invoice = Invoice.objects.get(pk=pk)
        form = InvoiceForm(request.user, request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect("accountant_dashboard:invoices")

        context = {'invoice':invoice, 'form':form}
        return render(request, template_name=self.template_name, context=context)



class RegulationView(View):
    template_name = "accountant_dashboard/facture_comp/reglements.html"
    
    def get(self, request, *args, **kwargs):
        regulations = Regulations.objects.all()
        form = RegulationsForm()
        context = {'regulations':regulations, 'form':form}
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = RegulationsForm(request.POST)
        
        if form.is_valid():
            payment_number = generate_payment_number()
            invoice = form.cleaned_data['invoice']
            student = form.cleaned_data['student']
            payment_method = form.cleaned_data['payment_method']
            amount_payment = form.cleaned_data['amount_payment']
            comment = form.cleaned_data['comment']
            
            regulation = Regulations(
                payment_number=payment_number,
                invoice=invoice,
                student=student,
                payment_method=payment_method,
                amount_payment=amount_payment,
                comment=comment
            )
            
            regulation.save()
            return redirect("accountant_dashboard:regulations")
        
        return redirect("accountant_dashboard:invoices")
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Regulations, pk=pk)
        instance.delete()
        return render(request, template_name=self.template_name)


class FinancialCommitmentView(View):
    template_name = "accountant_dashboard/facture_comp/engagement_financier.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)



