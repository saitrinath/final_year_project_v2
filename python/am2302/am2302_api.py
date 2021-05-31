import flask
from flask import request, jsonify
import am2302 as am
from flask_cors import CORS

print("Initializing Web Services API")
app = flask.Flask(__name__)
app.config["DEBUG"] = True


CORS(app)





print("Starting base web API path routing....")
@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
print("Successfull")


print("Starting AM2302 sensor web API routing")
@app.route('/API/sensors/am2302', methods=['GET'])
def api_all():
	temp,hum = am.get_data()
	data = {"temp":temp,"hum":hum}
	print(data)
	return jsonify(data)
print("Successfull")

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run(host='192.168.43.75')
