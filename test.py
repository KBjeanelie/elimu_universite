import requests

url = 'http://localhost:8000/api/assessments/'
response = requests.get(url)

if response.status_code == 200:
    assessments = response.json()
    print(assessments)
else:
    print(f"Error: {response.status_code}")
