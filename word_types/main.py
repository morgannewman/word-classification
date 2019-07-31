import json

with open("words_common.json", "r") as f:
    dictionary = json.load(f)

nouns_plural = []
nouns_singular = []
adjectives = []
adverbs = []
superlatives = []
verbs_past = []
verbs_present = []
verbs_progressive = []
verbs_transitive = []

for word, parts in dictionary.items():
    for part in parts:
        if part == "other":
            continue

        if part == "noun:plural":
            nouns_plural.append(word)
            continue
        if part == "noun:singular":
            nouns_singular.append(word)
            continue
        if part == "adjective":
            adjectives.append(word)
            continue
        if part == "adverb":
            adverbs.append(word)
            continue
        if part == "superlative":
            superlatives.append(word)
            continue
        if part == "verb:past":
            verbs_past.append(word)
            continue
        if part == "verb:present":
            verbs_present.append(word)
            continue
        if part == "verb:progressive":
            verbs_progressive.append(word)
            continue
        if part == "verb:transitive":
            verbs_transitive.append(word)


count = (
    len(nouns_plural)
    + len(nouns_singular)
    + len(adjectives)
    + len(adverbs)
    + len(superlatives)
    + len(verbs_past)
    + len(verbs_present)
    + len(verbs_progressive)
    + len(verbs_transitive)
)

print(count)
