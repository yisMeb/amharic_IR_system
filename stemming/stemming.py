import dict

def remove_prefix(word):
    w1=word
    num = round((len(word))/2)
    if(w1[0:num-1] == w1[num+1:len(w1)]):
            return w1[num+1:len(w1)]
        
    for prefix in dict.prefixes:
        if word.startswith(prefix):
            return word[len(prefix):]
    return word
        

def remove_postfix(word):
    for postfix in dict.postfixes:
        if(word.endswith(postfix)):
            if(postfix=="taalach" or postfix == "twal"): 
                word = word[:-len(postfix)]+"aa"
                return word
            else:
                return word[:-len(postfix)]
    return word
          
def remove_infix(word):
    length = len(word)
    
    for i in range(1, length - 1):
            
        if word[i] == 'a' and word[i-1] == word[i+2]: # Rule for CaC pattern. for words like temelalese, it removes 'la' and returns the remaining string
                return word[:i-1] + word[i+2:]
        if word[i] == 'a':
            left = word[:i]
            right = word[i+2:]

   
            min_length = min(len(left), len(right))
            if left[-min_length:] == right[:min_length]:
                return left[:-min_length] + right 
    return word

          
def stem(word):
    
    word = remove_prefix(word)
    word = remove_infix(word)
    word = remove_postfix(word)
    return word
