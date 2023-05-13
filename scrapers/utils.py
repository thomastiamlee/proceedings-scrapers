from urllib.request import Request, urlopen

def log(message):
    print(message)

def get_html(url):
    req = Request(
        url='https://aaai.org/proceeding/01-aaai-22-technical-tracks-1/', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    fp = urlopen(req)
    webpage = fp.read()
    html = webpage.decode("utf8")
    fp.close()
    return html