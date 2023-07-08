from urllib.request import Request, urlopen

import json

results_path = '../results/'

def log(message):
    print(message)

def get_html(url):
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    fp = urlopen(req)
    webpage = fp.read()
    html = webpage.decode("utf8")
    fp.close()
    return html

def write_result_to_file(results, file_name):
    json_object = json.dumps(results, indent=4, ensure_ascii=False).encode('utf8')
    with open(results_path + file_name, "w", encoding='utf8') as outfile:
        outfile.write(json_object.decode())