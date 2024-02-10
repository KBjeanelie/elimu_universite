from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.facturation_forms import InvoiceForm, RegulationsForm

from backend.models.facturation import Invoice, Regulations
from module_invoice_and_accounting.views import generate_invoice_number, generate_payment_number


class InvoiceView(View):
    template_name = "accountant_dashboard/facture_comp/factures.html"
    
    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.all()
        form = InvoiceForm()
        context = {'invoices':invoices, 'form':form}
        return render(request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice_number = generate_invoice_number()
            career = form.cleaned_data['career']
            item = form.cleaned_data['item']
            student = form.cleaned_data['student']
            comment = form.cleaned_data['comment']
            
            # Utilisation des valeurs récupérées pour créer une nouvelle instance de la facture
            invoice = Invoice(
                invoice_number=invoice_number,
                career=career,
                item=item,
                student=student,
                comment=comment
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
        context = {'invoice':invoice, 'regulation':regulation}
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



