import requests

teacher_id = 1  # À adapter à l'ID de l'enseignant souhaité
url = f'http://localhost:8000/school_management/teacher-schedule/{teacher_id}/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)  # Affiche les emplois du temps de l'enseignant
else:
    print('Erreur lors de la récupération des données.')
