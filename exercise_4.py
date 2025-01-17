import requests

items = []

for i in range(0,5):
    response = requests.get('https://catfact.ninja/fact')
    items.append(response.json()["fact"])

for item in items:
    print(item)