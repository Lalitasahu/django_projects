import requests
import json
from bs4 import BeautifulSoup as BS

url = "https://www.decathlon.in/p/8767675/men-shoes/canvas-skateboarding-longboarding-low-top-shoes-vulca-100-black?id=8767675&type=p"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
 'Accept-Language': 'en-US,en;q=0.5',
 'DNT': '1',
 'Sec-GPC': '1',
 'Connection': 'keep-alive',
 'Upgrade-Insecure-Requests': '1',
 'Sec-Fetch-Dest': 'document',
 'Sec-Fetch-Mode': 'navigate',
 'Sec-Fetch-Site': 'none',
 'Sec-Fetch-User': '?1',
 'Priority': 'u=1',
 'Pragma': 'no-cache',
 'Cache-Control': 'no-cache'}

res = requests.get(url,headers=headers)

soup = BS(res.text,'html.parser')

js = json.loads(soup.find('script',id='__NEXT_DATA__').text)
state = json.loads(js['props']['initialState'])
product_info = state['reducer']['productPage']


specification = {}
technical_info = {}
product_detail = {}

for i in product_info['activeProduct']['description']['informationConcept']['structuring']:
    specification[i['name']] = i['description']


for i in product_info['activeProduct']['description']['informationConcept']['technicalInformation']:
    technical_info[i['name']] = i['description']


for i in product_info['activeProduct']['description']['benefits']:
    product_detail[i['name']] = i['description']


