import requests
import json

url = 'http://localhost:8000/user_account/create-student-user/'
response = requests.get(url)

if response.status_code == 204:
    data = response.json()
    # Utilisation des données renvoyées
    for account in data:
        print(account)  # Ou traitez les données autrement
else:
    print(f"Erreur : {response.status_code} - {response.text}")
