from django.contrib import admin

from module_invoice_and_accounting.models import FinancialCommitment, Invoice, Item, Regulations 

# Register your models here.
admin.site.register(Item)
admin.site.register(Invoice)
admin.site.register(FinancialCommitment)
admin.site.register(Regulations)
# admin.site.register(Estimate)
# admin.site.register(Donation)
# 
# admin.site.register(TimeLine)
# admin.site.register(BillingBracket)