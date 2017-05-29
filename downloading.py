import urllib.request
from wikidata.client import Client

file = open("D:/Users/Opsymonroe/Desktop/base3.txt")
client = Client()
s = 0
for line in file:
    line = line[0: len(line) - 1]
    client = Client()
    entity = client.get(line, load = True)
    imagep = client.get('P18')
    image = entity[imagep]
    urllib.request.urlretrieve(image.image_url, "D:/Users/Opsymonroe/Images/botgeo/" + line + ".jpg")
    s += 1
    print(s)