def is_adj(s):
    return re.compile(r"^(a$|a |a\.|a\/|ad\.|adj.)").match(s)


def is_adv(s):
    return re.compile("^adv").match(s)


def is_conj(s):
    return re.compile(r"^conj\.").match(s)


def get_verb_tense(s):
    if re.compile(r"^imp\.").match(s):
        return "verb:past"
    if re.compile(r"^p\.? ?(p|a)").match(s):
        return "verb:progressive"
    if re.compile(r"^v\. i\.").match(s):
        return "verb:present"
    if re.compile(r"^v\. ?t"):
        return "verb:transitive"


def get_noun_tense(s):
    if re.compile(r"^(n\. ?pl\.?|pl\.)$").match(s):
        return "noun:plural"
    if re.compile(r"^n\.?").match(s):
        return "noun:singular"


def is_superlative(s):
    return re.compile(r"^sup").match(s)


def format_tense(tense):
    if tense == "":
        return "other"

    if is_adj(tense):
        return "adjective"

    if is_adv(tense):
        return "adverb"

    if is_superlative(tense):
        return "superlative"

    noun = get_noun_tense(tense)
    if noun:
        return noun

    verb = get_verb_tense(tense)
    if verb:
        return verb

    return "other"
