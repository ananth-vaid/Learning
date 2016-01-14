import requests
import xml.etree.ElementTree as ET

url = input('Enter - ')
xml = requests.get(url)
tree=ET.fromstring(xml.text)

counts = tree.findall('.//count')
count=0
for i in counts:
	count+=int(i.text)
print(count)
