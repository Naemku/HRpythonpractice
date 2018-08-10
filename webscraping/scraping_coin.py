import requests
from bs4 import BeautifulSoup

for adrs in ['bitcoin', 'ethereum', 'ripple']:
    url="https://coinmarketcap.com/currencies/"+adrs
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find(id="quote_price")
    price=table.find('span',attrs={"class":"h2 text-semi-bold details-panel-item--price__value"})
    print("{a} is now {b}$".format(a=adrs,b=price.text))
