import requests
from bs4 import BeautifulSoup


url="https://www.rottentomatoes.com/"
response=requests.get(url)
html=response.text
soup=BeautifulSoup(html,'html.parser')

table=soup.find(id="Top-Box-Office")
tr_table=table.find_all('tr')

for tr in tr_table:
    td_table=tr.find_all('td')
    score=td_table[0].find('span',attrs={'class':'tMeterScore'}).text
    name=td_table[1].a.text
    benefit=td_table[2].a.text
    print("Rottenscore: {a} / Title: {b} / Benefit: {c}".format(a=score,b=name,c=score)) 
