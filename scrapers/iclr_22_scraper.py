# Scraper for:
# ICML 2022 Main Conference Proceedings

from bs4 import BeautifulSoup
from utils import *

url = f'https://api.openreview.net/notes?content.venue=ICLR+2022+Oral&details=replyCount&offset=0&limit=1000&invitation=ICLR.cc%2F2022%2FConference%2F-%2FBlind_Submission'
output = 'iclr_22.json'

def execute():
    titles = []
    authors = []

    log('Scraping url: ' + url)
    html = get_html(url)
    records = json.loads(html)['notes']

    for record in records:
        title = record['content']['title']
        author = ', '.join(record['content']['authors'])
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