from indexing import build_index,save_index_to_json
import tokenization
import termweighting
import os
import re

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
def preprocess():
    doc_dir = './documents'
    
    amharic_pattern = re.compile('[\u1200-\u137F]+')
    
    for filename in os.listdir(doc_dir):
        file_path = os.path.join(doc_dir, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            filtered_content = ' '.join(amharic_pattern.findall(content))
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(filtered_content)
                
            print(f"Processed {filename}")


def main():
    
    preprocess()
    
    doc_dir = './documents'
    index_file = './indexed_doc.json'
    weighting = './termWeights.json'
    #tokenization
    tokens_by_file = tokenization.tokenize(doc_dir)
    #indexing
    index = build_index(tokens_by_file)
    save_index_to_json(index, index_file)
    
    # term weighting
    index = termweighting.load_index(index_file)
    tf_idf_scores = termweighting.calculate_tf_idf(index)
    termweighting.save_term_weights(tf_idf_scores, weighting)
    

         
if __name__ == "__main__":
    main()
