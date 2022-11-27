from bs4 import BeautifulSoup
import requests
import csv

count = 0
def getdata(url):
    r = requests.get(url)
    return r.text
dt = []
d1 = []
para = []
infobox = []
title = []
link = getdata("https://en.wikipedia.org/wiki/C._J._Cregg")
soup = BeautifulSoup(link, 'html.parser')
p = soup.find('h1').get_text()
k = soup.find('table')
x = soup.find_all('p')[1].get_text()
title.append(p)
if k is None:
    infobox.append('No InfoBox')
else:
    infobox.append(k.get_text())
para.append(x)

alllinks = soup.find_all("a", href = True, text = True)

link_text = ""
for d in alllinks:
    if d['href'].find("/wiki/") == -1:
        continue
    count += 1
    link_text = d['href']
    x = "https://en.wikipedia.org" + link_text
    link = getdata(x)
    soup = BeautifulSoup(link, 'html.parser')
    k = soup.find('table')
    p = soup.find('h1').get_text()
    x = soup.find_all('p')[1].get_text()
    title.append(p)
    if k is None:
        infobox.append('No InfoBox')
    else:
        infobox.append(k.get_text())
    para.append(x)
    if count == 10:
        break
   
 
datarow = []
count2 = 0
while count2 != 11:
    d = [title[count2], infobox[count2], para[count2]]
    datarow.append(d)
    count2 += 1
    
with open('wiki.csv', 'w', encoding ='UTF8') as f:
   writer = csv.writer(f)
   print(datarow)
   for row in datarow:
        writer.writerow(row)


