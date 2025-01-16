import json

# 1.2 Create python dictionary
item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100,
}

# 1.3 Encode python dictionary to JSON string
json_string = json.dumps(item)

# 1.4 Decode JSON string to Python dictionary
python_dict = json.loads(json_string)
print(item)
print(json_string)
print(python_dict)

# 1.5 Write JSON to a file
with open('json_file.json', 'w') as write_file:
    write_file.write(json_string)

# 1.6 Read JSON from a file:
with open('json_file.json') as read_file:
    json_object = json.load(read_file)

print(json_object)