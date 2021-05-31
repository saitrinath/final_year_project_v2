import Adafruit_DHT
import time
import os
import sys
sys.path.append('../')

import calculate.calc as calc
import mariadb_connector.sql as sql

DHT_SENSOR = Adafruit_DHT.AM2302

DHT_PIN=os.environ['am2302']

cur = sql.get_cur()

while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

	if humidity is not None and temperature is not None:
		temp = round(temperature,1)
		hum = round(humidity,1)
		thi = calc.calc_thi(temp,hum)
		cur.execute("insert into env_sensor_data(temperature,humidity,thi,time) values(?,?,?,now())",(temp,hum,thi))
		print('done')
		time.sleep(5)
