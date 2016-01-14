"""
import requests
from bs4 import BeautifulSoup

url = input('Enter - ')
html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")
sum=0
# Retrieve all of the anchor tags
tags = soup("span")
for text in tags:
    sum+=int(text.get_text())
print (sum)
"""

import requests
from bs4 import BeautifulSoup
import ssl

url = input('Enter main URL ')
pos = int(input('Position - '))
times = int(input('No. of times - '))

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
for i in range(0,times):
    html = requests.get(url,verify=False)
    soup = BeautifulSoup(html.text,"html.parser")
    tags = soup.find_all("a")
    url=tags[pos-1].get("href")
    value= tags[pos-1].get_text("a")   
print(value)