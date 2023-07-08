# Scraper for:
# ACL 2022 Main Conference Proceedings

from bs4 import BeautifulSoup
from utils import *

url = f'https://aclanthology.org/events/emnlp-2022'
output = 'emnlp_22.json'

def execute():
    titles = []
    authors = []
    links = []

    log('Scraping url: ' + url)
    html = get_html(url)

    soup = BeautifulSoup(html, 'html.parser')
    
    target = soup.find('div', attrs={'id': '2022emnlp-main'})
    
    for link in target.find_all('p', attrs={'class': 'd-sm-flex align-items-stretch'}):
        title = link.find('strong').text
        pdf_link = 'https://aclanthology.org' + link.find('strong').find('a', attrs={'class': 'align-middle'})['href']
        author_list = []
        target = link.find_all('span')
        ctr = 1
        for item in target:
            if ctr == 1:
                ctr -= 1
                continue
            for author in item.find_all('a', recursive=False):
                author_list.append(author.text)
        author = ', '.join(author_list)
        
        titles.append(title)
        authors.append(author)
        links.append(pdf_link)
    
    result = []
    for title, author, link in zip(titles, authors, links):
        result.append({
            'paper_title': title,
            'paper_link': link,
            'author_names': author
        })

    write_result_to_file(result, output)
    
execute()