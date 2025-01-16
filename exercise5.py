word_list = []

try:
    with open('words.txt') as file:
        for line in file:
            line = line.replace("\n", "")
            word_list.append(line)
except:
    print("There was en error when reading the file.")

alphabetically_sorted = sorted(word_list)
sorted_list = sorted(alphabetically_sorted, key=len)

try:
    with open('new words.txt', 'w') as file:
        for word in sorted_list:
            file.write(word + "\n")
except:
    print("There was an error when opening the file.")