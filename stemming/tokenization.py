import dict
import os
import re
def amharic_to_english_converter(amharic_text):
    translated_text = ""
    for char in amharic_text:
        if char in dict.amharic_to_english:
            translated_text += dict.amharic_to_english[char]
        else:
            translated_text += char   
    return translated_text

def tokenize(doc_dir):
    tokens_by_file = {}
    
    for filename in os.listdir(doc_dir):
        file_path = os.path.join(doc_dir, filename)
      
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            translated_text = amharic_to_english_converter(content)
            
            tokens = re.split(r'[ ,.\-_?]+', translated_text)
            tokens = [token for token in tokens if token]
            
            tokens_by_file[filename] = tokens
            print(f"Tokenized {filename}")

    return tokens_by_file

def tokenize_query(query):
    translated_query = amharic_to_english_converter(query)
    tokens = re.split(r'[ ,.\-_?]+', translated_query)
    tokens = [token for token in tokens if token] 
    return tokens
    