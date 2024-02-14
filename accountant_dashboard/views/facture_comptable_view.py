import datetime
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from backend.forms.facturation_forms import InvoiceForm, RepaymentForm, SpendForm
from backend.models.facturation import FinancialCommitment, Invoice, Repayment, Spend
from django.core.cache import cache
from django.db.models import Sum

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


class FinancialCommitmentView(View):
    template_name = "accountant_dashboard/facture_comp/engagement_financier.html"
    
    def get(self, request, *args, **kwargs):
        engagements = FinancialCommitment.objects.filter(school=request.user.school)
        context = {'engagements':engagements}
        return render(request, template_name=self.template_name, context=context)
    
    def send(self, pk, *args, **kwargs):
        engagement = FinancialCommitment.objects.get(pk=pk)
        engagement.send_date = now()
        engagement.is_send = True
        engagement.save()
        return redirect('accountant_dashboard:financials')
        


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
            amount = form.cleaned_data['amount']
            student = form.cleaned_data['student']
            comment = form.cleaned_data['comment']
            invoice_status = form.cleaned_data['invoice_status']
            
            # Utilisation des valeurs récupérées pour créer une nouvelle instance de la facture
            invoice = Invoice(
                invoice_number=invoice_number,
                career=career,
                item=item,
                amount=amount,
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
        context = {'invoice':invoice}
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


#=============================== PARTIE CONCERNANT LES REMBOURSEMENTS ==========================
class EditRepaymentView(View):
    template = "accountant_dashboard/facture_comp/editer_remboursement.html"
    def get(self, request, pk, *args, **kwargs):
        repayment = get_object_or_404(Repayment, pk=pk)
        form = RepaymentForm(request.user, instance=repayment)
        context = {'form':form, 'repayment':repayment}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        repayment = get_object_or_404(Repayment, pk=pk)
        data = request.POST.copy()
        data['school'] = request.user.school
        form = RepaymentForm(request.user, data, instance=repayment)
        if form.is_valid():
            form.save()
            return redirect('accountant_dashboard:repayments')  # Redirigez vers la page appropriée après la mise à jour réussie
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'repayment': repayment}
        return render(request, template_name=self.template, context=context)
    
class AddRepaymentView(View):
    template = "accountant_dashboard/facture_comp/ajout_remboursement.html"
    def get(self, request, *args, **kwargs):
        form = RepaymentForm(request.user)
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        invoice = Invoice.objects.get(school=request.user.school, pk=data['invoice'])
        data['amount'] = invoice.amount
        form = RepaymentForm(request.user, data)
        if form.is_valid():
            form.save()
            invoice.is_repayment = True
            invoice.save()
            return redirect("accountant_dashboard:repayments")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class RepaymentView(View):
    template = "accountant_dashboard/facture_comp/remboursements.html"

    def get(self, request, *args, **kwargs):
        repayments = Repayment.objects.filter(school=request.user.school).order_by('-created_at')
        context = {'repayments': repayments}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Repayment, pk=pk)
        instance.invoice.is_repayment = False
        instance.invoice.save()
        instance.delete()
        
        repayments = Repayment.objects.filter(school=request.user.school).order_by('-created_at')
        context = {'repayments': repayments}
        return render(request, template_name=self.template, context=context)
    
#===END

class DepenseView(View):
    template_name = "accountant_dashboard/rapport_financier/depenses.html"
    
    def get(self, request, *args, **kwargs):
        spends = Spend.objects.filter(school=request.user.school).order_by('-created_at')
        context = {'spends':spends}
        return render(request, template_name=self.template_name, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Spend, pk=pk)
        instance.delete()

        spends = Spend.objects.filter(school=request.user.school).order_by('-created_at')
        context = {'spends':spends}
        return render(request, template_name=self.template_name, context=context)
    

class AddDepenseView(View):
    template = "accountant_dashboard/rapport_financier/ajout_depense.html"
    
    def get(self, request, *args, **kwargs):
        form = SpendForm(request.user)
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['school'] = request.user.school
        form = SpendForm(request.user, data)
        if form.is_valid():
            form.save()
            return redirect("accountant_dashboard:spend")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class EditDepenseView(View):
    template = "accountant_dashboard/rapport_financier/editer_depense.html"
    
    def get(self, request, pk, *args, **kwargs):
        spend = Spend.objects.get(pk=pk)
        form = SpendForm(request.user, instance=spend)
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        data = request.POST.copy()
        spend = Spend.objects.get(pk=pk)
        data['school'] = request.user.school
        form = SpendForm(request.user, data, instance=spend)
        if form.is_valid():
            form.save()
            return redirect("accountant_dashboard:spend")
        
        context = {'form':form}
        return render(request, template_name=self.template, context=context)


class BalanceMonitoring(View):
    template_name = "accountant_dashboard/rapport_financier/suivi_solde.html"
    
    def get(self, request, *args, **kwargs):
        #recuperer l'ensemble des facture déjà totalement payé
        invoices = Invoice.objects.filter(school=request.user.school, invoice_status='Entièrement payé', is_repayment=False).order_by('-created_at')

        #recuperer le nombre total de facture payé
        count_invoices = Invoice.objects.filter(school=request.user.school, invoice_status='Entièrement payé', is_repayment=False).count()
        
        # Somme des montants des factures payées
        amount_payed = invoices.aggregate(total_montant=Sum('amount'))['total_montant'] or 0

        # Récupérer tous les engagements financiers
        engagements = FinancialCommitment.objects.filter(school=request.user.school)
        total_engagements = engagements.aggregate(total=Sum('school_fees'))['total'] or 0

        # Calcul du montant impayé
        not_payed = total_engagements - amount_payed

        context = {
            'invoices':invoices,
            'count_invoices':count_invoices,
            'amount_payed':amount_payed,
            'total_engagements':total_engagements,
            'not_payed':not_payed
        }
        return render(request, template_name=self.template_name, context=context)


