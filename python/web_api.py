import flask
from flask import request, jsonify
from flask_cors import CORS
import unidecode

import am2302.am2302 as am
import dht11.dht11 as dht
import heartrate.heart as hr
import mariadb_connector.sql as sql
import raspberry_info.system_info as si
import calculate.calc as calc

cur=sql.get_cur()

print("Initializing Web Services API")
app = flask.Flask(__name__)
app.config["DEBUG"] = True

temp_a=0
hum_a=0

CORS(app)


print("Starting web API home path routing....")
@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
print("Successfull")


@app.route('/API/system/info', methods=['GET'])
def api_system():
	cpu_usage,cpu_temp,cpu_freq,memory = si.get_server_stats()
	data={"cpu_usage":cpu_usage, "cpu_temp":cpu_temp, "cpu_freq":cpu_freq, "memory":memory}
	print(data)
	return jsonify(data)


@app.route('/API/sensors/heart_rate', methods=['GET'])
def api_heart_rate():
        rate = hr.get_data()
        data_heart = {"heart_rate":rate}
        print(data_heart)
        return jsonify(data_heart)

print("Starting AM2302 sensor web API routing")
@app.route('/API/sensors/am2302', methods=['GET'])
def api_am2302():
	temp,hum = am.get_data()
	data = {"temp":temp,"hum":hum}
	print(data)
	return jsonify(data)
print("Successfull")

@app.route('/API/sensors/am2302_thi', methods=['GET'])
def api_am2302_thi():
	temp,hum=am.get_data()
	thi=calc.calc_thi(temp,hum)
	data = {"thi":thi}
	print(data)
	return jsonify(data)


@app.route('/API/sensors/dht11', methods=['GET'])
def api_dht11():
        temp = dht.get_data()
        data_dht = {"temp":temp}
        print(data_dht)
        return jsonify(data_dht)

@app.route('/API/sensors/am2302_history', methods=['GET'])
def api_am_history():
	cur.execute("select * from env_sensor_data order by esdid desc limit 20")
	temp = []
	hum = []
	timee = []
	for a in cur:
		temp.append(a[1])
		hum.append(a[2])
		timee.append(a[4])
	data_am = {"temp":temp,"hum":hum,"time":timee}
	print(data_am)
	return jsonify(data_am)


@app.route('/API/weather/current', methods=['GET'])
def api_weather_current():
	cur.execute("select * from current_weather order by cwid desc limit 1")
	weather_data = []
	for a in cur:
		data=a
	place = unidecode.unidecode(data[1])
	date = str(data[7].day)+"-"+str(data[7].month)+"-"+str(data[7].year)
	data_weather = {"place":place,"temp":data[2],"hum":data[3],"thi":data[4],"description":data[5],"pressure":data[6],"log":date}
	print(data_weather)
	return jsonify(data_weather)




@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
	app.run(host='0.0.0.0')

