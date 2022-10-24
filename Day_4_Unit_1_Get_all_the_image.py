import re
import requests
from bs4 import BeautifulSoup
try:
    site = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    urls = [img['src'] for img in image_tags]
    for url in urls:
        filename = re.search(r'/([\w%_-]+[.](JPG|gif|svg|png|jpg))', url)
        if not filename:
            continue
        with open(filename.group(1), 'wb') as f:
            response = requests.get('https:' + url)
            f.write(response.content)
    print("Download complete, downloaded images can be found in current directory!")
except Exception:
    pass
