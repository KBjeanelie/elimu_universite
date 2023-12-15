import requests
import json

url = 'http://localhost:8000/educational_content/book_categories/'
response = requests.get(url)

if response.status_code == 204:
    data = response.json()
    # Utilisation des données renvoyées
    for account in data:
        print(account)  # Ou traitez les données autrement
else:
    print(f"Erreur : {response.status_code} - {response.text}")
