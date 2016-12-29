# FilmStat
############################
#   Script by Arkenopterix
############################
#  The purpose of this code is to log in a CSV file the press and viewer ratings of a film from the allocine website
#   in order to get stats on the rating trends of a film.
############################

import urllib.request
import sys
import datetime
from lxml import html
import os


def main(filename,urlnum):

    # build url variable
    url = "http://www.allocine.fr/film/fichefilm_gen_cfilm="+str(urlnum)+".html"
    file = os.getcwd() + "/" + filename +".csv"

    # get HTML data from the page
    page = html.fromstring(urllib.request.urlopen(url).read())

    spec = []
    specTemp = []

    # retrieve and format the ratings from the page and associate it to a time log

    for link in page.xpath("//span[@class='stareval-note']"):
        specTemp.append(link.text.lstrip('\n '))

    spec.append(datetime.datetime.now().isoformat())
    spec.append(specTemp[0].replace(',','.'))
    spec.append(specTemp[1].replace(',','.'))


    try:
        if os.path.exists(file):
            with open(file,"a") as fi:
                fi.write("\r"+spec[0]+","+spec[1]+","+spec[2])
                fi.close()
        else:
            with open(file, "a") as fi:
                fi.write("Date,Presse,Spectateurs")
                fi.write("\r" + spec[0] + "," + spec[1] + "," + spec[2])
                fi.close()
    except:
        print("Error while loading the file : "+sys.exc_info()[0])
        exit()
    print(spec)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: missing arguments")
        exit()
    main(str(sys.argv[1]),str(sys.argv[2]))
