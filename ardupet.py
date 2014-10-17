"""ArduPET is an office automation implementation. It is originally designed to
be use at the Tutorial Education Program (PET in pt-BR, hence the name) to turn
lights on and off and unlock the door, while also checking the statuses.

Routes:
GET /light -- lists all lamps statuses
GET /light/<id> -- get the status of the lamp identified by <id>
PUT /light/<id> -- update the status of the lamp identified by <id>
GET /door -- get the status of the door
PUT /door -- unlock the door (unlocking relocks after some seconds)
"""

import flask

app = flask.Flask(__name__)

@app.route('/lamp', methods=['GET'])
def lamp_index():
	"""Return a listing of all lamps statuses."""
	return '', 501

@app.route('/lamp/<int:light_id>', methods=['GET', 'PUT'])
def lamp_status(id):
	"""Read or update the status of a single lamp.

	Keyword arguments:
	id -- the id of the desired lamp.
	"""
	return '', 501

@app.route('/door', methods=['GET', 'PUT'])
def door_status():
	"""Read the status or update (unlock) the door."""
	return '', 501

if __name__ == "__main__":
	app.run()
