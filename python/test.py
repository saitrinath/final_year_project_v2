import multiprocessing
import mariadb_connector.sql as sql

import am2302.am2302 as am
import dht11.dht11 as dht
import calculate.calc as calc

import time

cur=sql.get_cur()

db_insert_delay=3

print("Number of cpu : ", multiprocessing.cpu_count())

def am2302_service():
	for a in range(100000):
		temp,hum = am.get_data()
		thi=calc.calc_thi(temp,hum)
		cur.execute("insert into env_sensor_live(temperature,humidity,thi) values(?,?,?)",(temp,hum,thi))
		print("done!  inserted am2302 data")
		time.sleep(db_insert_delay)



def dht11_service():
	for a in range(100000):
		temp = dht.get_data()
		cur.execute("insert into rt_sensor_live(temperature) values(?)",(temp,))
		print("done!  inserted dht11 data")
		time.sleep(db_insert_delay)

def clean_up(p1,p2):
	p1.terminate()
	p2.terminate()
	print("terminated p1,p2 processes!")

def mainn():
	print("Live Sensors Module Starting")
	p1 = multiprocessing.Process(target=am2302_service)
	p2 = multiprocessing.Process(target=dht11_service)
	p1.start()
	p2.start()
	print("Live Sensors Module Running!")

def alone():
	print("Live Sensors Module Starting")
	p1 = multiprocessing.Process(target=am2302_service)
	p2 = multiprocessing.Process(target=dht11_service)
	p1.start()
	p2.start()
	time.sleep(100000)
	p1.terminate()
	p2.terminate()
	p1.join()
	p2.join()
	print("Terminated")


if __name__ == "__main__":
	alone()
