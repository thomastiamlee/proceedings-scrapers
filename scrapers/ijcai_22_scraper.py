# Scraper for:
# IJCAI 2022 Main Conference Proceedings

from bs4 import BeautifulSoup
from utils import *

url = f'https://www.ijcai.org/proceedings/2022/'
output = 'ijcai_22.json'

def execute():
    titles = []
    authors = []

    log('Scraping url: ' + url)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('div', attrs={'class': 'paper_wrapper'}):
        title = link.find('div', attrs={'class': 'title'}).text
        author = link.find('div', attrs={'class': 'authors'}).text
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