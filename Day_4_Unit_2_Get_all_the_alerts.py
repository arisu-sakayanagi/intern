from bs4 import BeautifulSoup
import requests


url = 'https://www.us-cert.gov/ncas/alerts'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

links = []

for link in soup.find_all('a'):
    if link.get('href') != None:
        if link.get('href').startswith('/ncas/alerts/aa22'):
            links.append(link.get('href'))

count = 0

for i in range(0, len(links)):
    urls = 'https://www.cisa.gov/uscert' + links[i]
    print(urls)
    count+=1

print(count)
