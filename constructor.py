import urllib3
from bs4 import BeautifulSoup
import json

def askInput(placeholder):
    return str(input(placeholder+": "))

# saite, no kuras iegūst requestus
def getData(lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)
    except:
        return "ERROR: Numeric inputs only!"
    if lat <= -90 or lat >= 90: return "Invalid latitude"
    if lon <= -180 or lon >= 180: return "Invalid longitude"
    return 'https://nominatim.openstreetmap.org/reverse?format=geocodejson&lat='+str(lat)+'&lon='+str(lon)+'&zoom=18'

def printJSON(json):
    labels = ('name', 'type', 'housenumber', 'street', 'city', 'postcode', 'country', 'countrycode')
    for thing in labels:
        try:
            data = json['features'][0]['properties']['geocoding'][thing]
        except:
            continue
        print("{: >15} : {}".format(getCapitaled(thing), data))

def getCapitaled(word):
    return word[0].capitalize() + word[1:].lower()

def main():
    while (True):
        # vidzeme university coordinates!!
        # url = getData(57.541792843039296, 25.42830826616339)
        url = getData(askInput("Latitude"), askInput("Longitude"))
        if url.startswith("https") == False: 
            print(url)
            continue
        page = urllib3.PoolManager().request("GET", url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.data, "html.parser")
        data = json.loads(soup.text)
        printJSON(data)

if __name__== "__main__":
    main()