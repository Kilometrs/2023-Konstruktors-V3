import urllib3
from bs4 import BeautifulSoup
import json
import logging
import logging.config
import mysql.connector
import requests
import json
import datetime
import time
import yaml

from datetime import datetime
from configparser import ConfigParser
from mysql.connector import Error

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

def init_db():
	global connection
	connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)

def get_cursor():
	global connection
	try:
		connection.ping(reconnect=True, attempts=1, delay=0)
		connection.commit()
		logger.info("<CI2> CONNECTION TO DB SUCCESFULL!")
	except mysql.connector.Error as err:
		logger.error("<CI2.2> No connection to db " + str(err))
		connection = init_db()
		connection.commit()
	return connection.cursor()

#####
try:
    # Loading logging configuration
    with open('./log_worker.yaml', 'r') as stream:
        log_config = yaml.safe_load(stream)
    logging.config.dictConfig(log_config)

    # Creating logger
    logger = logging.getLogger('root')
except Exception as e: 
    print("<CE4> Could not initialize log config! LOGGING IS NOW DISABLED!!")
    print(e)
#####

#####
try:
    config = ConfigParser()
    config.read('config.ini')

    mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
    mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
    mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
    mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

except:
    logger.error("<CE1> Could not fetch databse data from config file!")
    logger.exception('')
#####

def main():
    init_db()

    # laiks tagad
    dt = datetime.now()
    request_date = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)  
    # print("Generated today's date: " + str(request_date))

    while (True):
        # vidzeme university coordinates!!
        # url = getData(57.541792843039296, 25.42830826616339)
        url = getData(askInput("Latitude"), askInput("Longitude"))
        if url.startswith("https") == False: 
            print(url)
            continue

        if logger != None: logger.info("<CI2> Request url: " + url)
        r = urllib3.PoolManager().request("GET", url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.data, "html.parser")
        data = json.loads(soup.text)
        printJSON(data)

if __name__== "__main__":
    main()