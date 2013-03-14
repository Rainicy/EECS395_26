import urllib
import HTMLParser
from BeautifulSoup import BeautifulSoup

def articleTextFromURL(url):
    page = urllib.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html)
    tags = soup.body.findAll('p')
    text_str = ""

    for tag in tags:
        text = tag.getText()
        text_str += text

    parser = HTMLParser.HTMLParser()
    text_str = parser.unescape(text_str)

    return text_str
