from django.db import models

from school_management.models import Career
from user_account.models import Student

# Create your models here.
# class Donation(models.Model):
    
#     donate_number = models.CharField(max_length=100)
    
#     donate_date = models.DateField()
    
#     donate_amount = models.FloatField()
    
#     reason_for_donation = models.TextField()
    
#     donate_year = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, null=True)
    
#     donate_type = models.CharField(max_length=20)
    
#     donor_name = models.CharField(max_length=50)
    
#     donor_firstname = models.CharField(max_length=50)
    
#     donor_address = models.CharField(max_length=50)
    
#     donor_postal_code = models.CharField(max_length=8)
    
#     donor_city = models.CharField(max_length=50)
    
#     donor_country = models.CharField(max_length=50)
    
#     donor_tel = models.CharField(max_length=20)
    
#     donor_email = models.CharField(max_length=120)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Don : {self.donor_name}"

    
# class BillingBracket(models.Model):
    
#     label = models.CharField(max_length=20)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Tranche de facturation : {self.label}"


# class TimeLine(models.Model):
    
#     label = models.CharField(max_length=20)
    
#     payment_month = models.CharField(max_length=20)
    
#     day_of_payment = models.CharField(max_length=20)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Echéancier : {self.label}"
    
    
class Item(models.Model):
    
    name = models.CharField(max_length=20)
    
    default_amount = models.IntegerField(default=0)
    
    defaut_quantity = models.IntegerField(default=1)
    
    #timline_model = models.ForeignKey(TimeLine, on_delete=models.SET_NULL, null=True)
    
    is_active = models.BooleanField(default=True)
    
    #submitted_to_tranche = models.BooleanField(default=True)
    
    analytic_code = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Article : {self.name}"
    
    
class Invoice(models.Model):
    
    invoice_number = models.CharField(max_length=50, unique=True)
    
    invoice_date = models.DateField(auto_now=True)
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True)
    
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    
    #timeline = models.ForeignKey(TimeLine, on_delete=models.DO_NOTHING)
    
    choices = [('Entièrement payé', 'Entièrement payé'), ('Non payé', 'Non payé'), ('Avance', 'Avance')]
    
    payment_status = models.CharField(max_length=20, choices=choices, blank=True)
    
    comment = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"N°{self.invoice_number}"


class Regulations(models.Model):
    
    payment_number = models.CharField(max_length=50, unique=True)
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    choices = [('Espèce', 'Espèce'), ('Chèque', 'Chèque')]
    payment_method = models.CharField(max_length=20, choices=choices, blank=True)
    
    date_payment = models.DateField(auto_now=True)
    
    amount_payment = models.IntegerField()
    
    comment = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)


# class Estimate(models.Model):
    
#     estimate_number = models.CharField(max_length=50, unique=True)
    
#     date_estimate = models.DateField()
    
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
#     career = models.ForeignKey(Career, on_delete=models.CASCADE)
    
#     item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    
#     timeline = models.ForeignKey(TimeLine, on_delete=models.DO_NOTHING)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     updated_at = models.DateTimeField(auto_now=True)


class FinancialCommitment(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    school_fees = models.IntegerField()
    
    send_date = models.DateTimeField(blank=True, null=True)
    
    is_send = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)