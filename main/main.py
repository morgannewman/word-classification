import json

with open("words.json", "r") as f:
    dictionary = json.load(f)

with open("main/common_0.txt", "r") as f:
    words = f.readlines()

abridged_dictionary = {}
count = 0
with open("main/common_1.json", "w") as f:
    for word in words:
        if "-" in word:
            continue


        word = word.rstrip('\n').title()
        if word not in dictionary:
            continue
        count += 1
        abridged_dictionary[word] = dictionary[word]

    json.dump(abridged_dictionary, f, indent=2)
