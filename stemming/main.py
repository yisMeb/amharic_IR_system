import tokenization
import stemming
import dict

def replace_with_rule(token, rule):
    for key, value in rule.items():
        token = token.replace(key, value)
    return token

def main():
    user_input = input("Enter Amharic text: ").strip()
    tokens = tokenization.tokenize(user_input)
    print("TOKEN: ",tokens)
    stemmed_tokens = [stemming.stem(token) for token in tokens]
    stem = [replace_with_rule(token, dict.Rule) for token in stemmed_tokens]
    print("STEM:", ' , '.join(stem))

   
    
if __name__ == "__main__":
    main()


