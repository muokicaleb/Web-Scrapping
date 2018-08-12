"""
using beautifulsoup to extract only the h1 headers
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())

print(bsObj.h1)
# bsObj.html.body.h1
# bsObj.body.h1
# bsObj.html.h1
