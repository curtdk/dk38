import requests
from bs4 import BeautifulSoup

# res = requests.get(url)
# print(res.status_code)

def getHtmlList(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.textpip
    except:
        print("1")
    
res=getHtmlList('https://poocoin.app/tokens/0x768a62a22b187eb350637e720ebc552d905c0331')
print(res)
# soup = BeautifulSoup(res, 'html.parser')
# title = soup.title.text 
# print(title)