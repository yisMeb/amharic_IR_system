import dict

def remove_prefix(word):
    for prefix in dict.prefixes:
        if word.startswith(prefix):
            return word[len(prefix):]
    return word

def remove_postfix(word):
    for postfix in dict.postfixes:
        if word.endswith(postfix):
            return word[:-len(postfix)]
    return word

def stem(word):
    word = remove_prefix(word)
    word = remove_postfix(word)
    return word
