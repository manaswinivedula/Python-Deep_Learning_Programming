import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Deep_learning"
source=requests.get(url)
text=source.text
soup=BeautifulSoup(text,"html.parser")
print(soup.title.string)
b=(soup.find_all('a'))
for link in b:
    print(link.get('href'))
