import Adafruit_DHT
import time
import os
DHT_SENSOR = Adafruit_DHT.AM2302

DHT_PIN = os.environ['am2302']

def get_data():

	while True:
		humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

		if humidity is not None and temperature is not None:
			temp = round(temperature,1)
			hum = round(humidity,1)
			return temp,hum
