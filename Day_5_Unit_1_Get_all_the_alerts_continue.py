from bs4 import BeautifulSoup
import requests
import csv, re


url = 'https://www.us-cert.gov/ncas/alerts'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

links = []

for link in soup.find_all('a'):
    a = link.get('href')
    if a != None:
        if a.startswith('/ncas/alerts/aa22'):
            links.append('https://www.cisa.gov/uscert' + a)


with open('alert.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['Alert Link', 'Alert ID', 'Alert Name', 'Release Date', 'Last revised', 'Tips'])
    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        alertId= soup.select('#page-title')
        alertId =  ''.join(re.findall(r'.{4}-.{4}',alertId[0].getText()))
        alertName = soup.select('#page-sub-title')
        alertName = alertName[0].getText()
        regexRelease =re.compile(r'Original release date: (.*)?')
        releaseDate = soup.select('.submitted.meta-text')
        releaseDate = releaseDate[0].getText().strip()
        releaseDate = regexRelease.search(releaseDate)
        releaseDate = releaseDate.group(1).split('|')[0]
        regexRevised = re.compile(r'Last revised: (.*)?')
        revised = soup.select('.submitted.meta-text')
        revised = revised[0].getText().strip()
        revised = regexRevised.search(revised)
        if revised == None:
            revised = ""
        else:
            revised = revised.group(1).strip()
        tip = soup.find('p', class_= "tip-intro")
        if tip == None:
            tip = ""
        else:
            tip = tip.getText()

        writer.writerow([link, alertId, alertName, releaseDate, revised, tip])
        
