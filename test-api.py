import requests

# URL de l'API
url = 'http://localhost:8000/educational_content/ebooks/1/'


# Envoi de la requête GET
response = requests.get(url)

# Vérification du statut de la réponse
if response.status_code == 200:
    # Affichage des fichiers récupérés
    files = response.json()
    print("Fichiers récupérés :")
    for file in files:
        print(file)
else:
    print("La requête n'a pas abouti. Code de statut :", response.status_code)
