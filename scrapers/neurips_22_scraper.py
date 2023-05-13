# Scraper for:
# NeurIPS 2022 Main Conference Proceedings
# NOTE: Papers under the datasets and benchmarks track are
# implemented in a separate scraper.

from bs4 import BeautifulSoup
from utils import *

url = f'https://papers.nips.cc/paper_files/paper/2022'
output = 'neurips_22.json'

def execute():
    titles = []
    authors = []

    log('Scraping url: ' + url)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('li', attrs={'class': 'conference'}):
        title = link.find('a').text
        author = link.find('i').text
        titles.append(title)
        authors.append(author)

    result = []
    for title, author in zip(titles, authors):
        result.append({
            'paper_title': title,
            'author_names': author
        })

    write_result_to_file(result, output)

execute()