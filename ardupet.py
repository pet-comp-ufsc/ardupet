"""ArduPET is an office automation implementation. It is originally designed to
be use at the Tutorial Education Program (PET in pt-BR, hence the name) to turn
lamps on and off and unlock the door, while also checking the statuses.

Routes:
GET /lamp -- lists all lamps statuses
GET /lamp/<id> -- get the status of the lamp identified by <id>
PUT /lamp/<id> -- update the status of the lamp identified by <id>
GET /door -- get the status of the door
PUT /door -- unlock the door (unlocking relocks after some seconds)
"""

import flask
import serial
import codes

app = flask.Flask(__name__)
arduino = serial.Serial('/dev/ttyACM0', 9600)

@app.route('/lamp', methods=['GET'])
def lamp_index():
	"""Return a listing of all lamps statuses."""
	return '', 501

@app.route('/lamp/<int:lamp_id>', methods=['GET', 'PUT'])
def lamp_status(id):
	"""Read or update the status of a single lamp.

	Keyword arguments:
	id -- the id of the desired lamp.
	"""
	message = 'Lamp is '
	code = codes.codes['lamps'][id]
	if flask.request.method == 'GET':
		"""Bytes sent are: operation (r), target (l), id"""
		call = ''.join(['r', 'l', chr(id)])

		arduino.write(bytes(call, 'ASCII'))
		status = ord(arduino.read())

		message = ''.join([message, status and 'on' or 'off'])

	return message, 200

@app.route('/door', methods=['GET', 'PUT'])
def door_status():
	"""Read the status or update (unlock) the door."""
	return '', 501

if __name__ == "__main__":
	app.run()
