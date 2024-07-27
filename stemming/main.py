import tokenization
import stemming


def main():
    user_input = input("Enter Amharic text: ").strip()
    tokens = tokenization.tokenize(user_input)
    print("Token: ",tokens)
    stemmed_tokens = [stemming.stem(token) for token in tokens]
    print("Stemmed text:", ' '.join(stemmed_tokens))
   
    
if __name__ == "__main__":
    main()

