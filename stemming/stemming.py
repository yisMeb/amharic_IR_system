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

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        words = infile.read().split()
        
    # Remove prefixe
    prefix_removed = [remove_prefix(word) for word in words]
    
    # Remove postfixes
    processed_words = [remove_postfix(word) for word in prefix_removed]
    
    with open(output_file_path, 'w') as outfile:
        outfile.write('\n'.join(processed_words))
            
def stem(word):
    word = remove_prefix(word)
    word = remove_postfix(word)
    return word
