import shelve
import urllib
from wikidata.client import Client

file  = open("D:/Users/Opsymonroe/Desktop/base2.txt")


base = shelve.open("D:/Users/Opsymonroe/Documents/botgeobase/geobase")
ind = 0
for line in file:
    line  = line[0: len(line)-1]
    client = Client()
    entity = client.get(line, load=True)
    str = str(entity.attributes)
    indexlat = str.find('latitude')
    s = str[indexlat + 11: indexlat + 100]
    del str
    mas = s.split(',')
    length = float(mas[0])
    long = mas[1][13: len(mas[1])]
    lon = float(long)
    list = [length, lon]
    base[line] = list
    ind += 1
    print(ind)