"""import requests
import json
url = input('Enter main URL ')
response = requests.get(url)
json_back = response.json()
sum=0
for comment in json_back["comments"]:
	sum+=comment["count"]
print(sum)	
"""
import requests
import json

url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    payload = {"sensor":"false","address":address}
    response=requests.get(url,params=payload)

    json_back=response.json()
    print(json_back["results"][0]["place_id"])


import requests
import urllib

url = 'http://python-data.dr-chuck.net/geojson?'

while True:
	test = urllib.urlopen(url).read()
	test_url=url = url + urllib.urlencode({'sensor':'false', 'address': address})
    address = input('Enter location: ')
    if len(address) < 1 : break
    payload = {"sensor":"false","address":address}
    response=requests.get(url,params=payload)

    json_back=response.json()
    print(json_back["results"][0]["place_id"])
