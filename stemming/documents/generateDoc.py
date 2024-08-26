import os
import requests
from bs4 import BeautifulSoup

def scrape_voa_amharic_articles(base_url, max_pages=20, num_documents=100):
   
    if not os.path.exists('documents'):
        os.makedirs('documents')
    
    doc_count = 0
    page = 1 

    while page <= max_pages and doc_count < num_documents:
        url = f'{base_url}?p={page}'
        source_code = requests.get(url)

        if source_code.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {source_code.status_code}")
            break
        
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

     
        articles = soup.find_all('div', class_='media-block')

        if not articles:
            print(f"No articles found on page {page}.")
            break
        
        for article in articles:
            if doc_count >= num_documents:
                break

            
            link_tag = article.find('a', href=True)
            if link_tag:
                article_url = link_tag['href']
                full_article_url = f"https://amharic.voanews.com{article_url}"
                article_response = requests.get(full_article_url)

                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')

                    
                    article_content = article_soup.find('div', class_='wsw')
                    if article_content:
                        
                        article_text = article_content.get_text(separator="\n", strip=True)
                        
                        
                        doc_filename = f'documents/document_{doc_count + 1}.txt'
                        with open(doc_filename, 'w', encoding='utf-8') as f:
                            f.write(article_text)
                        
                        print(f"Saved {doc_filename}")
                        doc_count += 1
                else:
                    print(f"Failed to retrieve article. Status code: {article_response.status_code}")

        page += 1

    print(f"Scraping completed. {doc_count} documents were saved.")

base_url = 'https://amharic.voanews.com/z/3661'

scrape_voa_amharic_articles(base_url, max_pages=20, num_documents=100)
