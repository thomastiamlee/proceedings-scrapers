# Scraper for:
# AAAI 2022 Main Conference Proceedings

from bs4 import BeautifulSoup
from utils import *

urls = [f'https://aaai.org/proceeding/{str(i).zfill(2)}-aaai-22-technical-tracks-{i}/' for i in range(1,11)]
output = 'aaai_22.json'

def execute():
    titles = []
    authors = []

    for url in urls:
        log('Scraping url: ' + url)
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        for link in soup.find_all('li', attrs={'class': 'paper-wrap'}):
            titles.append(link.find('a').text)
            authors.append(link.find('span').find('p').text)
        
    result = []
    for title, author in zip(titles, authors):
        result.append({
            'paper_title': title,
            'author_names': author
        })

    write_result_to_file(result, output)
    
execute()