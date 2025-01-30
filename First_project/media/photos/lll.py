import json
from requests import Session
from bs4 import BeautifulSoup as BS
s = Session()

s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def calling(url):
    lk = []
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    links = soup.find_all('a')
    for i in links:
        lnk = url.replace(url.split('/')[-1],"")+i.get('href')
        print(lnk)
        new_l = calling(lnk)
        if new_l[lnk]:
            lk.append(calling(lnk))
        else:
            lk.append(lnk)
    return {url:lk}


def crawl(url):
    datas = {}
    data = frozenset(datas.items())
    # url = "http://webserver.rilegislature.gov//Statutes/TITLE2/INDEX.HTM"
    # data[url] = calling(url)
    # return data
    try:
        r = s.get(url)
        soup = BS(r.text,'html.parser')
        for i in soup.find_all('a','homeLinks'):
            data[i.get('href')] = (calling(i.get('href')))
    except:
        data = "NA"
    return data

url = "http://webserver.rilegislature.gov/Statutes/"

x = crawl(url)

with open('file1.json','w') as file:
    file.write(json.dumps(x,indent=4))



"""

   ...: def calling(url):
   ...:     lk = []
   ...:     r = s.get(url)
   ...:     soup = BS(r.text,'html.parser')
   ...:     links = soup.find_all('a')
   ...:     for i in links:
   ...:         lnk = url.replace(url.split('/')[-1],"")+i.get('href')
   ...:         print(lnk)
   ...:         new_l = calling(lnk)
   ...:         if new_l[lnk]:
   ...:             lk.append(calling(lnk))
   ...:             # return
   ...:         else:
   ...:             lk.append(lnk)
   ...:     return {url:lk}


"""