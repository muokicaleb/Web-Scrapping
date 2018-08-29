from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""we have included exceptions to check if the page is available
and if the tags have the correct formatting"""


def getTitle(url):
    # to check if the server is up and the page is available on the server
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    # to check if the correct tages have been used
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title is None:
    print("Title could not be found")
else:
    print(title)
