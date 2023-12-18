import requests

url = 'http://localhost:8000/api/login/'
data = {
    'username': 'admin',
    'password': 'azerty123',
}

#data = {'student_id': 1}
response = requests.post(url, data=data)

if response.status_code == 201:  # Code HTTP 201 : Création réussie
    print(response.json())  # Affiche les données de l'objet créé
else:
    print('Erreur lors de la création de l\'objet :', response.status_code)
    print(response.json())  # Affiche les éventuelles erreurs de validation
