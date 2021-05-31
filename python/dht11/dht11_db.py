import sys
import Adafruit_DHT
import time
import os
pin = os.environ['dht11']

import sys
sys.path.append('../')

import mariadb_connector.sql as sql

cur = sql.get_cur()

while True:
	humidity, temp = Adafruit_DHT.read_retry(11, pin)
	cur.execute("insert into rt_sensor_data(temperature,time) values(?,now())",(temp,))
	print("inserted : ",temp)
	time.sleep(5)
