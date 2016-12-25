#import urllib.request
#with urllib.request.urlopen('http://www.allocine.fr/film/fichefilm_gen_cfilm=228094.html') as response:
#   html = response.read()
#print(html)
import urllib
import urllib.request
import sys
import datetime
from lxml import html


url = 'http://www.allocine.fr/film/fichefilm_gen_cfilm=228094.html'
page = html.fromstring(urllib.request.urlopen(url).read())
stat = []
spec = []
specTemp = []

for link in page.xpath("//span[@class='stareval-note']"):
    specTemp.append(link.text.lstrip('\n '))
    #print("Name", link.text, "URL", link.get("href"))
spec.append(datetime.datetime.now().isoformat())
spec.append(specTemp[0].replace(',','.'))
spec.append(specTemp[1].replace(',','.'))

try:
    with open("/home/brieg/Projects/FilmStat/testfilm.csv","a") as fi:
        fi.write("\r"+spec[0]+","+spec[1]+","+spec[2])
        fi.close()
except:
    print("Error while loading the file : "+sys.exc_info()[0])
    exit()
print(spec)


