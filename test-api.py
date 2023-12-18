import requests

# Remplacez 'VOTRE_TOKEN_JWT' par votre token JWT valide
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyOTc2MzU0LCJpYXQiOjE3MDI4ODk5NTQsImp0aSI6ImI5YTJjYjZkNGQzMDRhMTViNTY5YTdjNDBhMWRkMTc3IiwidXNlcl9pZCI6MX0.OZBYH5k2zZzS54QjqE0Qheis-w_ygYzviRlmDZph0fc'
headers = {
    'Authorization': f'Bearer {token}'
}

url = 'http://localhost:8000/educational_content/books/'  # Remplacez par votre URL

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)  # Faites quelque chose avec les données retournées
else:
    print(f"Erreur: {response.status_code}")
    print(response.text)  # Affiche la réponse d'erreur du serveur
