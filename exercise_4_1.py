import requests
import json

response = requests.get('https://api.github.com/search/repositories?q=language:python')
data = response.json()

for i in sorted(data['items'], key=lambda x: x['forks'], reverse=True):
    print(f'Forks:{i["forks"]}. Name:{i["name"]} Description:{i["description"]}')