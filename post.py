import requests

url = 'http://localhost:8000/user_account/manager-account-view/'
data = {
    'username': 'gestionnaire',
    'password': 'azerty',
    'manager_id': 5, 
    'is_active': True
}

#data = {'student_id': 1}
response = requests.delete(url, data=data)

if response.status_code == 204:  # Code HTTP 201 : Création réussie
    print('Suppression reussi !')
    print(response.json())  # Affiche les données de l'objet créé
else:
    print('Erreur lors de la création de l\'objet :', response.status_code)
    print(response.json())  # Affiche les éventuelles erreurs de validation
