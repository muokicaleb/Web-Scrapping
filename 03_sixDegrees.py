"""
A program to find the number of links it would take  from Eric Idle to Kevin Bacon

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://en.wikipedia.org/wiki/kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
