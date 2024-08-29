import tkinter as tk
from tkinter import messagebox
import os
import re
import json
from indexing import build_index, save_index_to_json
import tokenization
import stemming
import termweighting
import dict

# Helper functions
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

# Preprocessing function
def preprocess():
    #change this one to your location
    doc_dir = 'stemming\documents'
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

# Stemming input function
def stem_input(user_input):
    tokens = tokenization.tokenize_query(user_input)
    stem = [replace_with_rule(token, dict.Rule) for token in tokens]
    stemmed_tokens = [
        stemming.stem(token) if token not in dict.exceptions else token
        for token in stem
    ]
    return stemmed_tokens

# Query processing function
def process_query(query):
    doc_dir = 'stemming\documents'
    stemmed_query = stem_input(query)
    document_scores = {}

    for term in stemmed_query:
        if term in term_weights:
            for doc, weight in term_weights[term].items():
                if doc in document_scores:
                    document_scores[doc] += weight
                else:
                    document_scores[doc] = weight

    # Sort documents by their accumulated score in descending order
    sorted_docs = sorted(document_scores.items(), key=lambda x: x[1], reverse=True)

    results = []
    for doc, _ in sorted_docs[:5]:  # Limiting to top 5 results
        doc_path = os.path.join(doc_dir, doc)
        try:
            with open(doc_path, 'r', encoding='utf-8') as file:
                preview = ' '.join(file.read().split()[:50])  # Short preview of the document
            results.append({"doc": doc, "preview": preview})
        except FileNotFoundError:
            print(f"File not found: {doc_path}")

    return results

# Function to open a document in a new window
def open_document_window(doc_path):
    def go_back():
        doc_window.destroy()
        root.deiconify()  # Show the main window again

    root.withdraw()  # Hide the main window

    doc_window = tk.Toplevel(root)
    doc_window.title(doc_path)

    with open(doc_path, 'r', encoding='utf-8') as file:
        content = file.read()

    text = tk.Text(doc_window, wrap=tk.WORD, width=80, height=30)
    text.insert(tk.END, content)
    text.pack()

    back_button = tk.Button(doc_window, text="ተመለስ", command=go_back)
    back_button.pack()

# Search query function
def search_query():
    query = entry.get().strip()
    
    if not query:
        messagebox.showwarning("ያስገቡት ነገር ላይ ችግር አለ", "መፈለግ የሚፈልጉትን ያስገቡ!")
        return

    results = process_query(query)
    result_text.delete(1.0, tk.END)

    if results:
        for result in results:
            doc_path = os.path.join(doc_dir, result['doc'])
            link = tk.Label(result_text, text=result['doc'], fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", lambda e, p=doc_path: open_document_window(p))
            result_text.window_create(tk.END, window=link)
            result_text.insert(tk.END, f"\nPreview: {result['preview']}...\n\n")
    else:
        result_text.insert(tk.END, "ምንም አልተገኘም!")

# Launch the GUI
def launch_gui():
    global entry, result_text, root, term_weights, doc_dir

    root = tk.Tk()
    root.title("አማርኛ መረጃ መፈለግያ")

    # Load the term weights from the JSON file
    with open('termWeights.json', 'r', encoding='utf-8') as file:
        term_weights = json.load(file)
    
    doc_dir = 'stemming\documents'

    # Create the input field
    label = tk.Label(root, text="መፈለግ የሚፈልጉትን ያስገቡ:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    # Create the search button
    search_button = tk.Button(root, text="ፈልግ", command=search_query)
    search_button.pack(pady=5)

    # Create the results display area
    result_text = tk.Text(root, wrap=tk.WORD, width=100, height=20)
    result_text.pack(pady=10)

    root.mainloop()

def main():
    preprocess()
    
    doc_dir = 'stemming\documents'
    index_file = './indexed_doc.json'
    weighting = './termWeights.json'
    
    tokens_by_file = tokenization.tokenize(doc_dir)
    
    index = build_index(tokens_by_file)
    save_index_to_json(index, index_file)
    
    index = termweighting.load_index(index_file)
    tf_idf_scores = termweighting.calculate_tf_idf(index)
    termweighting.save_term_weights(tf_idf_scores, weighting)
    
    launch_gui()

if __name__ == "__main__":
    main()
