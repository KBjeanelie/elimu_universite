import requests
import json

# Les données à envoyer dans la requête PUT
data = {
     "invoice_date": "2023-11-12",
    "payment_status": "Payé entièrement",
    "comment": 'Bon etudiant',  # Mettre à null pour la date actuelle
}

# ID de l'engagement financier à mettre à jour
invoice_id = 1  # Remplacez par l'ID de l'engagement financier spécifique

# L'URL pour la mise à jour de l'engagement financier
url = f"http://localhost:8000/module_invoice_and_accounting/invoices/{invoice_id}/"

# Envoi de la requête PUT avec les données
response = requests.patch(url, json=data)

# Vérification de la réponse
if response.status_code == 200:
    print("La facture a été mis à jour avec succès !")
else:
    print("Échec de la mise à jour de l'engagement financier :", response.text)
