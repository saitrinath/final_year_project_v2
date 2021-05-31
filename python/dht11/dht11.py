import sys
import Adafruit_DHT
import time
import os

pin=os.environ['dht11']
print(pin)
def get_data():
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, pin)

		if humidity is not None and temperature is not None:
			temp = round(temperature,1)
			return temp
