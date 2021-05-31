import random
import time

import sys
sys.path.append('../')

import mariadb_connector.sql as sql

cur = sql.get_cur()


for i in range(10):
	hr = random.randint(64,66)
	print(hr)
	cur.execute("insert into heart_rate_data(heart_rate,time) values(?,now())",(hr,))
	time.sleep(3)
