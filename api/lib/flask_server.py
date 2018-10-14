from flask import Flask, request
from google_cloud_api import localize_objects_uri
from google_cloud_api import detect_labels_uri
app = Flask(__name__)
@app.route('/json', methods=['POST']) #GET requests will be blocked
def json_example():
	req_data = request.get_json()
	uri = req_data["uri"]
	response = ""
	response = response+detect_labels_uri(uri)+" "
	response = response+localize_objects_uri(uri)
	return '''{}'''.format(response)
if __name__ == '__main__':
	app.run(host="192.168.43.184",port=5000)

