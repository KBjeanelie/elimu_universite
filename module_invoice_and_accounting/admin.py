from django.contrib import admin

from module_invoice_and_accounting.models import BillingBracket, Donation, Estimate, FinancialCommitment, Invoice, Item, Payment, TimeLine

# Register your models here.
admin.site.register(Item)
admin.site.register(Invoice)
admin.site.register(FinancialCommitment)
admin.site.register(Estimate)
admin.site.register(Donation)
admin.site.register(Payment)
admin.site.register(TimeLine)
admin.site.register(BillingBracket)