from django.shortcuts import render
from django.views import View


class InvoiceView(View):
    template_name = "accountant_dashboard/facture_comp/factures.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)



class RegulationView(View):
    template_name = "accountant_dashboard/facture_comp/reglements.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class FinancialCommitmentView(View):
    template_name = "accountant_dashboard/facture_comp/engagement_financier.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)



