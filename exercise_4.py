import requests

new_list = []

for i in range(1,6):
    x = requests.get('https://catfact.ninja/fact')
    data = x.json()

    new_list.append(data)

for item in new_list:
    print(item)