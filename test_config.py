import os
import requests
import mysql.connector

from datetime import datetime
from configparser import ConfigParser

print("Configuration file test")

# Testing if configuration file exists on disk in the current working directory
print("----------")
print("Checking if config file exists -->")
assert os.path.isfile("config.ini") == True
print("OK")
print("----------")

# Opening the configuration file
config = ConfigParser()
config.read('config.ini')

# Checking if all MYSQL related config options are present in the config file
print("Checking if config has MYSQL related options -->")
assert config.has_option('mysql_config', 'mysql_host') == True
assert config.has_option('mysql_config', 'mysql_db') == True
assert config.has_option('mysql_config', 'mysql_user') == True
assert config.has_option('mysql_config', 'mysql_pass') == True
print("OK")
print("----------")

# Checking if possible to connect to the URL
print("Checking if it is possible to get data from the site -->")
lon, lat = 57.541792843039296, 25.42830826616339
r = requests.get('https://nominatim.openstreetmap.org/reverse?format=geocodejson&lat='+str(lat)+'&lon='+str(lon)+'&zoom=18')
assert r.status_code == 200
print("OK")
print("----------")

# Checking if possible to connect to MySQL with the existing config options
print("Checking if it is possible to connect to MYSQL with the given config options -->")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("----------")

# Checking if log config files exist for log config
print("Checking if DB migration component log config file exists log_migrate_db.yaml -->")
assert os.path.isfile("log_migrate_db.yaml") == True
print("OK")
print("----------")
print("Checking if asteroid worker component log config file exists log_worker.yaml -->")
assert os.path.isfile("log_worker.yaml") == True
print("OK")
print("----------")
print("Checking if log destination directory exists -->")
assert os.path.isdir("log") == True
print("OK")
print("----------")
print("Checking if migration source directory exists -->")
assert os.path.isdir("migrations") == True
print("OK")
print("----------")
print("Configuration file test DONE -> ALL OK")
print("----------------------------------------")