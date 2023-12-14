import requests
import json

# Les données à envoyer dans la requête POST
data = {
    "student": 1,
    "school_fees": 250000
}

# L'URL de l'API
url = "http://localhost:8000/module_invoice_and_accounting/financial-commitment/"

# En-têtes de la requête
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "X-CSRFToken": "vFPDfgMvHEEq1a268ZTDGwYu0PfjFZoGTs2DFuiTZa7tZwuFeIcQDlFARkqT3NRP"
}

# Envoi de la requête POST avec les données et les en-têtes
response = requests.post(url, headers=headers, data=json.dumps(data))

# Vérification de la réponse
if response.status_code == 201:
    print("Engagement financier créé avec succès !")
    financial_commitment = response.json()  # Récupération des données de l'engagement financier créé
    print("ID de l'engagement financier créé:", financial_commitment)
else:
    print("Échec de la création de l'engagement financier :", response.text)
