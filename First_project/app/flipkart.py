import requests
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd
s = Session()
# s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:10Gecko/20100101 Firefox/104.0'
cookies = {
    'T': 'TI173814816054500096425180886110423244776740381402225379889107149947',
    'SN': 'VIE1D67CA4BE6745CA8717430CF5E49336.TOK7A56A04FAD704DACB198FB0911749BC4.1739513658638.LO',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3NDExNTg0NDksImlhdCI6MTczOTQzMDQ0OSwiaXNzIjoia2V2bGFyIiwianRpIjoiZjQxNWFhYTItOGNlNi00ODY5LTkyMWYtNDNhODRiZjM3YTVkIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzM4MTQ4MTYwNTQ1MDAwOTY0MjUxODA4ODYxMTA0MjMyNDQ3NzY3NDAzODE0MDIyMjUzNzk4ODkxMDcxNDk5NDciLCJrZXZJZCI6IlZJRTFENjdDQTRCRTY3NDVDQTg3MTc0MzBDRjVFNDkzMzYiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.OuZhNsnBu-oKs9R6c3PAWd4Nmt-rTXXMkafvIPz6x7Y',
    'K-ACTION': 'null',
    'ud': '6.1BHr8qcPK3luPJDMU8a0xU-5euWGwb3H1aj-Oo64fHqx5vIlqfPINY4CFcKWeMETEU5PLujx6oaf4UnlcwKyfXwJqfWGs66MfyGW_879POUKpxhpkx21Dh0kCDF2RtxSgAh0UorxTQ1bJDqbs_2FoNIYGDCHYG0FZAEUH3ebZ8EE290TrENP0-U2V6DCWqWyvHRH3PwvE-XsAsJzi1KWXg11s9Bs4NWSj6kNpIWGVkSxcigzDZrXANfmB9YNfvC4NzBDFwwffrcUUpuGKvFu00xrqdDaCuFzM-G8MA5fxIg',
    'vh': '607',
    'vw': '1280',
    'dpr': '2',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20133%7CMCMID%7C49889531479391050572396254759899411558%7CMCAID%7CNONE%7CMCOPTOUT-1739437651s%7CNONE%7CMCAAMLH-1740035251%7C12%7CMCAAMB-1740035251%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
    'rt': 'null',
    'vd': 'VIE1D67CA4BE6745CA8717430CF5E49336-1738148198950-15.1739513658.1739512113.158816196',
    'S': 'd1t13Pz8/P3g/U1U/P1cqSl52P5T/P1KCpMD9C16hoOlfC0hE3FAaqcnVlnXQiRKcKvE+z2F3h5mUsYTBlwvy+qeHjQ==',
    'fonts-loaded': 'en_loaded',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fsearch%25253Fcount%25253D40%252526otracker%25253DCLP_filters%252526p%2525255B%2525255D%25253Dfacets.smart_tv%252525255B%252525255D%2525253DYe%2526ot%253DA',
    'qH': 'acc05e33fb140cc4',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.flipkart.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI173814816054500096425180886110423244776740381402225379889107149947; SN=VIE1D67CA4BE6745CA8717430CF5E49336.TOK7A56A04FAD704DACB198FB0911749BC4.1739513658638.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3NDExNTg0NDksImlhdCI6MTczOTQzMDQ0OSwiaXNzIjoia2V2bGFyIiwianRpIjoiZjQxNWFhYTItOGNlNi00ODY5LTkyMWYtNDNhODRiZjM3YTVkIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzM4MTQ4MTYwNTQ1MDAwOTY0MjUxODA4ODYxMTA0MjMyNDQ3NzY3NDAzODE0MDIyMjUzNzk4ODkxMDcxNDk5NDciLCJrZXZJZCI6IlZJRTFENjdDQTRCRTY3NDVDQTg3MTc0MzBDRjVFNDkzMzYiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.OuZhNsnBu-oKs9R6c3PAWd4Nmt-rTXXMkafvIPz6x7Y; K-ACTION=null; ud=6.1BHr8qcPK3luPJDMU8a0xU-5euWGwb3H1aj-Oo64fHqx5vIlqfPINY4CFcKWeMETEU5PLujx6oaf4UnlcwKyfXwJqfWGs66MfyGW_879POUKpxhpkx21Dh0kCDF2RtxSgAh0UorxTQ1bJDqbs_2FoNIYGDCHYG0FZAEUH3ebZ8EE290TrENP0-U2V6DCWqWyvHRH3PwvE-XsAsJzi1KWXg11s9Bs4NWSj6kNpIWGVkSxcigzDZrXANfmB9YNfvC4NzBDFwwffrcUUpuGKvFu00xrqdDaCuFzM-G8MA5fxIg; vh=607; vw=1280; dpr=2; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20133%7CMCMID%7C49889531479391050572396254759899411558%7CMCAID%7CNONE%7CMCOPTOUT-1739437651s%7CNONE%7CMCAAMLH-1740035251%7C12%7CMCAAMB-1740035251%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; rt=null; vd=VIE1D67CA4BE6745CA8717430CF5E49336-1738148198950-15.1739513658.1739512113.158816196; S=d1t13Pz8/P3g/U1U/P1cqSl52P5T/P1KCpMD9C16hoOlfC0hE3FAaqcnVlnXQiRKcKvE+z2F3h5mUsYTBlwvy+qeHjQ==; fonts-loaded=en_loaded; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fsearch%25253Fcount%25253D40%252526otracker%25253DCLP_filters%252526p%2525255B%2525255D%25253Dfacets.smart_tv%252525255B%252525255D%2525253DYe%2526ot%253DA; qH=acc05e33fb140cc4; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage',
    'Priority': 'u=0, i',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = [
    ('count', '40'),
    ('otracker', 'CLP_filters'),
    ('p[]', 'facets.smart_tv%5B%5D=Yes'),
    ('p[]', 'facets.resolution%5B%5D=Ultra+HD+%284K%29'),
    ('sid', 'ckf/czl'),
    ('otracker', 'nmenu_sub_TVs and Appliances_0_Smart and Ultra HD'),
    ('otracker', 'nmenu_sub_TVs & Appliances_0_Smart & Ultra HD'),
]


def detailpage(url):
    r = s.get(url)
    soup = bs(r.text, 'html.parser')

    try:
        title = soup.find('h1','_6EBuvT').text
    except:
        title = ''
    try:
        price = soup.find('div','Nx9bqj').text
    except:
        price = ''
    
    try:
        dis_price = soup.find('div','yRaY8j').text
    except:
        dis_price = ''

    try:
        description = soup.find('div','yN+eNk w9jEaj').text
    except:
        description = ''
    
    try:
        sp = soup.find_all('table', class_='_0ZhAN9')
        tr = [row for i in sp for row in i.find_all('tr', class_='WJdYP6 row')]
        key = [j.find('td', class_='+fFi1w col col-3-12').text for j in tr]
        value = [j.find('td', class_='Izz52n col col-9-12').text for j in tr]
        Specifications = dict(zip(key, value))

        # for i in soup.find_all('table', class_='_0ZhAN9'):
        #     for j in i.find_all('tr', class_='WJdYP6 row'):
        #         key = j.find('td', class_='+fFi1w col col-3-12').text
        #         value = j.find('td', class_='Izz52n col col-9-12').text
        #         Specifications = {
        #             key: value
        #         }
    except:
        Specifications = ''
    
    images = []
    try:
        for i in soup.find('div', class_='j9BzIm').find('ul').find_all('li'):
            img_src = i.find('img', class_='_0DkuPH').get('src').replace('/128/128/', '/416/416/')
            images.append(img_src)
    except:
        images = []

    detail_data = {
        'title':title,
        'price':price,
        'dis_price':dis_price,
        'description':description,
        'images':images,
        
    }
    detail_data.update(Specifications)
    return detail_data
l =[]
def listpage():
    response = requests.get('https://www.flipkart.com/search', params=params, cookies=cookies, headers=headers)
    soup = bs(response.text,'html.parser')

    all_pro = soup.find_all('div','tUxRFH')
    # all_pro = soup.find_all('div','hCKiGj')
    for pro in all_pro:
        links = 'https://www.flipkart.com'+pro.find('a','CGtC98').get('href')
        # links = 'https://www.flipkart.com'+pro.find('a','WKTcLC').get('href')
        
        detail = detailpage(links)
        data = {
            'links':links
        }
        data.update(detail)

        print(data)
        l.append(data)
listpage()

df = pd.DataFrame(l)
df.to_csv('Smart TV.csv', index=False)


