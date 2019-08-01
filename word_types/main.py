import json

with open("words_common.json", "r") as f:
    dictionary = json.load(f)

dicts = {
    "noun_plural": [],
    "noun_singular": [],
    "adjective": [],
    "adverb": [],
    "superlative": [],
    "verb_past": [],
    "verb_present": [],
    "verb_progressive": [],
}

for word, parts in dictionary.items():
    for part in parts:
        if part == "other":
            continue
        if part == "verb:transitive":
            continue

        if part == "noun:plural":
            dicts["noun_plural"].append(word)
            continue
        if part == "noun:singular":
            dicts["noun_singular"].append(word)
            continue
        if part == "adjective":
            dicts["adjective"].append(word)
            continue
        if part == "adverb":
            dicts["adverb"].append(word)
            continue
        if part == "superlative":
            dicts["superlative"].append(word)
            continue
        if part == "verb:past":
            dicts["verb_past"].append(word)
            continue
        if part == "verb:present":
            dicts["verb_present"].append(word)
            continue
        if part == "verb:progressive":
            dicts["verb_progressive"].append(word)
            continue


for name, words in dicts.items():
    with open("word_types/{}.json".format(name), "w") as f:
        json.dump(words, f, indent=2)
