import math
import json

def load_index(index_file):
    with open(index_file, 'r', encoding='utf-8') as file:
        index = json.load(file)
    return index

def calculate_tf_idf(index):
    Idf = {}
    Tf = {}
    TfIdf = {}
    docCount = len(index)
    
    for doc, terms in index.items():
        term_freq = {}
        term_count = len(terms)
        for term in terms:
            if term not in term_freq:
                term_freq[term] = 0
            term_freq[term] += 1
        
        Tf[doc] = {term: count / term_count for term, count in term_freq.items()}
        
        for term in term_freq:
            if term not in Idf:
                Idf[term] = 1
            else:
                Idf[term] += 1
    
    
    for term in Idf:
        Idf[term] = math.log2(docCount / Idf[term])
    
    for doc in Tf:
        TfIdf[doc] = {}
        for term in Tf[doc]:
            TfIdf[doc][term] = Tf[doc][term] * Idf[term]
    
    return TfIdf


def save_term_weights(tf_idf_scores, output_file):
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(tf_idf_scores, file, ensure_ascii=False, indent=4)
    print(f"Term weights saved to {output_file}")
    
    