#import urllib.request
#with urllib.request.urlopen('http://www.allocine.fr/film/fichefilm_gen_cfilm=228094.html') as response:
#   html = response.read()
#print(html)
import urllib
import urllib.request
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
spec.append(float(specTemp[0].replace(',','.')))
spec.append(float(specTemp[1].replace(',','.')))
print(spec)
