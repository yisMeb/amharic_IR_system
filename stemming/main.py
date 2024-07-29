import tokenization
import stemming
import dict

def replace_with_rule(token, rule):
    for key, value in rule.items():
        token = token.replace(key, value)
    return token

def main():
    user_input = input("Enter text: ").strip()
    tokens = tokenization.tokenize(user_input)
    print("TOKEN: ",tokens)
    stem = [replace_with_rule(token, dict.Rule) for token in tokens]
   
    stemmed_tokens = [
        stemming.stem(token) if token not in dict.exceptions else token
        for token in stem
    ]   
    print("STEM:", ' , '.join(stemmed_tokens))
    
    
if __name__ == "__main__":
    main()


