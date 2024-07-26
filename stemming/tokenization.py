import dict

def amharic_to_english_converter(amharic_text):
    translated_text = ""
    for char in amharic_text:
        if char in dict.amharic_to_english:
            translated_text += dict.amharic_to_english[char]
        else:
            translated_text += char   
    return translated_text

def tokenize(text):
    translated_text = amharic_to_english_converter(text)
    return translated_text.split()
