import tokenization
import stemming
import dict

def replace_with_rule(token, rule):
    for key, value in rule.items():
        token = token.replace(key, value)
    return token

def is_amharic(user_input):
    return any('\u1200' <= char <= '\u137F' for char in user_input)

def pair_consonant_with_vowel(stemmed_token, reverse_dict):
    amharic_word = ""
    i = 0
    while i < len(stemmed_token):
        for length in range(min(3, len(stemmed_token) - i), 0, -1):
            substring = stemmed_token[i:i + length]
            if substring in reverse_dict:
                amharic_word += reverse_dict[substring]
                i += length - 1
                break
        else:
            amharic_word += stemmed_token[i]
        i += 1
    return amharic_word

def main():
    user_input = input("Enter text: ").strip()
    is_amh = is_amharic(user_input)
    tokens = tokenization.tokenize(user_input)
    stem = [replace_with_rule(token, dict.Rule) for token in tokens]
    stemmed_tokens = [
        stemming.stem(token) if token not in dict.exceptions else token
        for token in stem
    ]
    
    if is_amh:
        amh = {v: k for k, v in dict.amharic_to_english.items()}
        answer = [pair_consonant_with_vowel(token, amh) for token in stemmed_tokens]
        print("STEM:", ' , '.join(answer))
    else:
        print("STEM:", ' , '.join(stemmed_tokens))
        
if __name__ == "__main__":
    main()


