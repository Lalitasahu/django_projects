import requests
from requests import Session
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:10Gecko/20100101 Firefox/104.0'
url = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=d85bff0a-3e59-46e4-ac18-21f6c8a40ea5'
r = s.get(url)
soup = bs(r.text,'html.parser')
l =[]
for pro in soup.find_all('div','tUxRFH'):
    link = 'https://www.flipkart.com'+pro.find('a').get('href') 

    r1 = s.get(link)
    soup1 = bs(r1.text,'html.parser')

    name = soup1.find('h1').text
    price = soup1.find('div','Nx9bqj').text
    dis_price = soup1.find('div','yRaY8j').text
    for t in soup.find_all('table'):
        for row in t.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 2:
                key = cols[0].text.strip()
                value = cols[1].text.strip()
                #if key == " Brand":
                #   brands.append(value)
                
    # brand = 
    # model 
    # storage
    # description
    # is_available

# df = pd.DataFrame(l)
# df.to_csv('flipkart.csv', index=False)