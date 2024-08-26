import os
import json
import dict
from stemming import stem


def remove_stopwords(tokens):
    return [token for token in tokens if token not in dict.stop_word_list]

def build_index(tokens_by_file):
    index = {}
    
    for filename, tokens in tokens_by_file.items():
        tokens = remove_stopwords(tokens)
        
        for token in tokens:
            stemmed_token = stem(token)
            if stemmed_token not in index:
                index[stemmed_token] = []
            if filename not in index[stemmed_token]:
                index[stemmed_token].append(filename)
    
    return index

def save_index_to_json(index, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(index, file, ensure_ascii=False, indent=4)
    print(f"Index saved to {output_file}")
