# import requests

# teacher_id = 1  # À adapter à l'ID de l'enseignant souhaité
# url = f'http://localhost:8000/school_management/teacher-schedule/{teacher_id}/'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)  # Affiche les emplois du temps de l'enseignant
# else:
#     print('Erreur lors de la récupération des données.')

import uuid
import datetime
import random

def convertir_en_hexadecimal(nombre):
    # Utiliser la fonction hex() pour convertir le nombre en hexadécimal
    nombre_hexadecimal = hex(nombre)
    
    # La fonction hex() renvoie une chaîne qui commence par '0x', nous la supprimons
    nombre_hexadecimal = nombre_hexadecimal[2:]
    
    return nombre_hexadecimal

def generer_nui(position):
    # Obtenir l'année actuelle
    annee_actuelle = datetime.datetime.now().year

    # Générer un nombre aléatoire entre 0 et 9
    nombre_aleatoire = random.randint(1, 10000000000000)
    
    r = convertir_en_hexadecimal(nombre_aleatoire)

    # Créer le NUI en utilisant le format spécifié
    nui = f"ELM-{annee_actuelle}-STD-{r.upper()}"
    
    return nui

# Exemple d'utilisation
nui_unique = generer_nui()
print("NUI généré :", nui_unique)


