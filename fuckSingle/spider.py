from bs4 import BeautifulSoup
import requests

def start(url):
    res = requests.get(url)
    print(res.encoding)
    html = res.content.decode(res.encoding)
    print(html)
    bsObj = BeautifulSoup(html,"lxml")
    print(bsObj)

start("http://www.youzh.me")
