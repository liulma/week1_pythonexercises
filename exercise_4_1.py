import requests
import json

x = requests.get('https://api.github.com/search/repositories?q=language:python')
data = x.json()

for item in data["items"]:
    forks = item["forks"]
    name = item["name"]
    description = item["description"]
    print(f"Forks:{forks}. Name:{name} Description:{description}")