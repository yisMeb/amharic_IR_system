import dict

def amharic_to_english_converter(amharic_text):
    translated_text = ""
    for char in amharic_text:
        if char in dict.amharic_to_english:
            translated_text += dict.amharic_to_english[char]
        else:
            translated_text += char   
    return translated_text

def amharic_file_to_english(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        amharic_text = infile.read()
    
    converted_text = amharic_to_english_converter(amharic_text)
    
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(converted_text)
      
        
def tokenize(text):
    translated_text = amharic_to_english_converter(text)
    return translated_text.split()
