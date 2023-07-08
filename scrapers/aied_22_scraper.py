# Scraper for:
# ACL 2022 Main Conference Proceedings

from bs4 import BeautifulSoup
from utils import *
import unicodedata

urls = [f'https://link.springer.com/book/10.1007/978-3-031-11644-5',
       f'https://link.springer.com/book/10.1007/978-3-031-11644-5?page=2#toc',
       f'https://link.springer.com/book/10.1007/978-3-031-11644-5?page=3#toc']
output = 'aied_22.json'

def execute():
    titles = []
    authors = []
    links = []

    for url in urls:
        log('Scraping url: ' + url)    
        html = get_html(url)

        soup = BeautifulSoup(html, 'html.parser')
        
        ctr = 0
        for link in soup.find_all('h4', attrs={'class': 'c-card__title'}):
            title = link.text
            pdf_link = link.find('a')
            if pdf_link is None: continue
            pdf_link = 'https://link.springer.com' + pdf_link['href']
            author = link.parent.find('ul', attrs={'class': 'c-author-list'}).text

            titles.append(title.strip())
            authors.append(author.strip())
            links.append(pdf_link)

            ctr = ctr + 1
            if url == 'https://link.springer.com/book/10.1007/978-3-031-11644-5?page=3#toc' and ctr == 2:
                break

    result = []
    for title, author, link in zip(titles, authors, links):
        result.append({
            'paper_title': title,
            'paper_link': link,
            'author_names': author
        })

    write_result_to_file(result, output)
    
execute()