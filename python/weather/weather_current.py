import requests, json
import sys
sys.path.append('../')
import os
import mariadb_connector.sql as sql
import calculate.calc as calc

cur = sql.get_cur()


api_key = os.environ['weather_aut']

base_url = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_key}"
city_code = '1277909'
complete_url = base_url.format(city_id=city_code,API_key=api_key)
response = requests.get(complete_url)
x = response.json()
def convert_to_celsius(n):
	return n-273.15
def get_weather():

	if x["cod"] != "404":

		y = x["main"]
		place = x["name"]
		cord = x["coord"]


		temp_k = y["temp"]

		pressure = y["pressure"]

		humidity = y["humidity"]

		z = x["weather"]

		weather_description = z[0]["description"]

		temp_c=convert_to_celsius(temp_k)
		thi=calc.calc_thi(temp_c,humidity)

		cur.execute("insert into current_weather(place,temperature, humidity,thi,weather_desc,pressure,day) values(?,?,?,?,?,?,curdate());",(place,temp_c,humidity,thi,weather_description,pressure))

		return temp_c,humidity,weather_description,pressure

	else:
		print(" City Not Found ")
		return "Error check city and http request"
get_weather()
