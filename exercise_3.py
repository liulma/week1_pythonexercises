import json

# 3.2 Create python dictionary
item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100
}
print("Python dictionary:")
print(item)

# 3.3 Encode python dictionary to JSON string
json_string = json.dumps(item)
print("\nPython dictionary encoded to JSON string:")
print(json_string)

# 3.4 Decode JSON string to Python dictionary
python_dict = json.loads(json_string)
print("\nJson string decoded to Python dictionary:")
print(python_dict)

# 3.5 Write JSON to a file
with open('json_file.json', 'w') as write_file:
    write_file.write(json_string)

# 3.6 Read JSON from a file:
with open('json_file.json') as read_file:
    json_object = json.load(read_file)
print("\n Read JSON from a file:")
print(json_object)

# 3.2.1 Add key-value pair to Python object
item["price"] = 1000

# 3.2.2 Add new array to Python object
item["sellers"] = ["John", "Peter", "Mary"]

# 3.2.3 Add new object to Python object
item["description"] = {
    "text": "This is a book of knowledge",
    "author": "Unknown",
    "importantPages": [33, 44, 555]
}

# 3.2.4 Print out item variable
print("\nItem variable:")
print(item)

# 3.2.5 Print out price from the object
print("\nPrice variable:")
print(item["price"])

# 3.2.6 Print out Peter from the array
print("\nPeter from sellers:")
print(item["sellers"][1])

# 3.2.7 Print out 555 from your Python object
print("\nPage 555 from importantPages:")
print(item["description"]["importantPages"][2])

# 3.2.8 Print out in one line
desc = item["description"]["text"]
bookmark = item["description"]["importantPages"][2]
print(f"\nDescription: {desc}\nBookmarked page: {bookmark}")

# 3.2.9 Remove price, seller and description from the Python object
del item["price"]
del item["sellers"]
del item["description"]
print("\n Python object after deletion of price, sellers and description:")
print(item)