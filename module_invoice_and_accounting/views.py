import datetime
from django.core.cache import cache
from module_invoice_and_accounting.models import *
from module_invoice_and_accounting.serializers import *

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

