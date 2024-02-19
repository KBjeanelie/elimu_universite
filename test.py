import requests
data_login = {
    'username': 'kbjeanelie',
    'password': 'azerty'
}

token = {
    'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODk0NjkxOSwiaWF0IjoxNzA4MzQyMTE5LCJqdGkiOiIwMWMxZGMwMGQ3YjE0NDA0YmExNzYwYmM4YTI2ZDZmOSIsInVzZXJfaWQiOjE1fQ.IsUUIuszpOsSxxCUWm_373yCnbbLQBwNO-3FqyHUAVQ', 
    'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NDI4NTE5LCJpYXQiOjE3MDgzNDIxMTksImp0aSI6ImRiMzNkZDNkNmVhODQ2OGRhZDMzMzcxNmIxYzg4YmU2IiwidXNlcl9pZCI6MTV9.g-Dwtk9PgDZ0lB8V_IxBzHxCmUT1nZNxVxvyj_JjwdI'
}

url = 'http://localhost:8000/api/parcours/'

headers = {'Authorization': 'Bearer ' + token['access']}  # Utilisez le jeton d'accès dans le dictionnaire token

response = requests.get(url, headers=headers)

if response.status_code == 200:
    assessments = response.json()
    print(assessments)
else:
    print(f"Error: {response.json()}")
