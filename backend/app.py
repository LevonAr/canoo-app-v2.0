import dotenv
import os
from bson import json_util, ObjectId
from datetime import datetime
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for,
    make_response,
    jsonify,
)
import pytz

from controllers.data_controller import *
from database import get_collection
from flask_cors import CORS, cross_origin

dotenv.load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

tz_LA = pytz.timezone('America/Los_Angeles')

@app.route("/")
def home():
    return jsonify("hello world!")


@app.route("/list_lights", methods=["GET"])
@cross_origin(supports_credentials=True)
def list_lights():
    """
    This is GET request API which list all the lights records from database.

    ----------

    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """
    response = all_lights_controller(filters={}, db_conn=get_collection('lights'))
    return jsonify(response)


@app.route("/add_light", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_light():
    """
    This is POST request API which insert the light records to database.

    ----------

    Request Parameters:

    - parameter name: light_name
      type: string
      required: True

    - parameter name: light_state
      type: Bool
      required: True

    - parameter name: light_color
      type: string
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "POST":
        print('------------')
        if not all(param in request.json for param in ['light_name', 'light_state', 'light_color']):
            raise jsonify("Parameter are missing to save light")
        light_name = request.json.get('light_name')
        light_color = request.json.get('light_color')
        light_state = request.json.get('light_state')
        print(datetime.now(tz_LA).replace(tzinfo=None).replace(tzinfo=None))
        data = dict(light_name=light_name, light_state=light_state, light_color=light_color, created_on=datetime.now(tz_LA).replace(tzinfo=None).replace(tzinfo=None))
        response = add_light_controller(payload=data, db_conn=get_collection('lights'))
        if response['success']:
            event_description = "Added " + light_name
            history_data = dict(appliance_type="Light", appliance_name=light_name, event_type='Add', created_on=datetime.now(tz_LA).replace(tzinfo=None).replace(tzinfo=None),
                                light_state=light_state, event_description=event_description, light_id=response['id'])
            add_history_controller(payload=history_data, db_conn=get_collection('history'))

        return jsonify(response)


@app.route("/update_light", methods=["POST"])
@cross_origin(supports_credentials=True)
def update_light():
    """
    This is POST request API which update the light record to database.

    ----------

    Request Parameters:

    - parameter name: id
      type: Alphanumeric
      required: True

    - parameter name: light_state
      type: Bool
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "POST":
        light_state = request.json.get('light_state')
        light_id = request.json.get('id')
        data = dict(light_state=light_state)

        current_state = get_existing_state(name="lights", filters={"_id": ObjectId(light_id)},
                                           db_conn=get_collection('lights'))

        db = get_collection('lights')
        db["lights"].update_one({"_id": ObjectId(light_id)}, {"$set": data})
        print("lights updated successfully!")
        ret = db["lights"].find_one({"_id": ObjectId(light_id)})

        state = "ON" if light_state else "OFF"
        event_description = "Updated from " + str(current_state["state"]) + " to " + str(state)
        history_data = dict(appliance_type="Light", appliance_name=ret['light_name'], event_type='Update', created_on=datetime.now(tz_LA).replace(tzinfo=None),
                            light_state=light_state, event_description=event_description, light_id=light_id)
        add_history_controller(payload=history_data, db_conn=get_collection('history'))

        return jsonify({"id": light_id, "message": "Light updated successfully"})


@app.route("/delete_light/<light_id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_light(light_id):
    """
    This is DELETE request API which remove the light record from database.

    ----------

    Request Parameters:

    - parameter name: id
      type: Alphanumeric
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "DELETE":
        db = get_collection('lights')
        # get the name of light before deleting
        ret = db["lights"].find_one({"_id": ObjectId(light_id)})
        if not ret:
          return {
            'success': False,
            'message': 'Light does not exist'
          }
        light_name = ret['light_name']
        light_state = ret['light_state']

        db["lights"].delete_one({"_id": ObjectId(light_id)})
        print("lights deleted successfully!")

        # save the logs
        event_description = "Deleted light " + light_name
        history_data = dict(appliance_type="Light", appliance_name=light_name, event_type='Delete', created_on=datetime.now(tz_LA).replace(tzinfo=None),
                            light_state=light_state, event_description=event_description, light_id=light_id)
        add_history_controller(payload=history_data, db_conn=get_collection('history'))
        return jsonify({"id": light_id, "message": "Light deleted successfully"})


@app.route("/list_thermostat", methods=["GET"])
@cross_origin(supports_credentials=True)
def list_thermostat():
    """
    This is GET request API which list all the thermostat records from database.

    ----------

    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    response = all_thermostat_controller(filters={}, db_conn=get_collection('thermostat'))
    return jsonify(response)


@app.route("/add_thermostat", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_thermostat():
    """
    This is POST request API which insert the thermostat records to database.

    ----------

    Request Parameters:

    - parameter name: thermostat_name
      type: string
      required: True

    - parameter name: temperature
      type: string
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "POST":
        if not all(param in request.json for param in ['thermostat_name', 'temperature']):
            raise jsonify("Parameter are missing to save thermostat")

        thermostat_name = request.json.get('thermostat_name')
        temperature = request.json.get('temperature')
        data = dict(thermostat_name=thermostat_name, temperature=temperature, created_on=datetime.now(tz_LA).replace(tzinfo=None))
        response = add_thermostat_controller(payload=data, db_conn=get_collection('thermostat'))
        if response['success']:
            event_description = "Added " + thermostat_name
            history_data = dict(appliance_type="Thermostat", appliance_name=thermostat_name, event_type='Add', created_on=datetime.now(tz_LA).replace(tzinfo=None),
                                temperature=temperature, event_description=event_description,
                                thermostat_id=response['id'])
            add_history_controller(payload=history_data, db_conn=get_collection('history'))
        return jsonify(response)


@app.route("/update_thermostat", methods=["POST"])
@cross_origin(supports_credentials=True)
def update_thermostat():
    """
    This is POST request API which update the thermostat records to database.

    ----------

    Request Parameters:

    - parameter name: id
      type: Alphanumeric
      required: True

    - parameter name: temperature
      type: string
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "POST":
        temperature = request.json.get('temperature')
        temperature_id = request.json.get('id')
        data = dict(temperature=temperature)
        current_state = get_existing_state(name="thermostat", filters={"_id": ObjectId(temperature_id)},
                                           db_conn=get_collection('thermostat'))
        db = get_collection('thermostat')
        db["thermostat"].update_one({"_id": ObjectId(temperature_id)}, {"$set": data})
        ret = db["thermostat"].find_one({"_id": ObjectId(temperature_id)})

        event_description = "Updated from " + str(current_state["temperature"]) + " to " + str(temperature)
        history_data = dict(appliance_type="Thermostat", appliance_name=ret['thermostat_name'], event_type='Update', created_on=datetime.now(tz_LA).replace(tzinfo=None),
                            temperature=temperature, event_description=event_description, thermostat_id=temperature_id)
        add_history_controller(payload=history_data, db_conn=get_collection('history'))

        return jsonify({"id": temperature_id, "message": "Thermostat updated successfully"})


@app.route("/delete_thermostat/<thermostat_id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_thermostat(thermostat_id):
    """
    This is DELETE request API which remove the thermostat record from database.

    ----------

    Request Parameters:

    - parameter name: id
      type: Alphanumeric
      required: True

    ----------


    Returns

    type: JSON

    description: Response object containing a message with 200 status code

    -------

    """

    if request.method == "DELETE":
        db = get_collection('thermostat')
        ret = db["thermostat"].find_one({"_id": ObjectId(thermostat_id)})
        if not ret:
          return {
            'success': False,
            'message': 'Thermostat does not exist'
          }

        db["thermostat"].delete_one({"_id": ObjectId(thermostat_id)})
        print("Thermostat deleted successfully!")

        event_description = "Deleted thermostat " + ret['thermostat_name']
        history_data = dict(appliance_type="Thermostat", appliance_name=ret['thermostat_name'], event_type='Delete', created_on=datetime.now(tz_LA).replace(tzinfo=None),
                            temperature=ret['temperature'], event_description=event_description, thermostat_id=thermostat_id)
        add_history_controller(payload=history_data, db_conn=get_collection('history'))
        return jsonify({"id": thermostat_id, "message": "Thermostat deleted successfully"})


@app.route("/logs", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_history():
    response = all_history_controller(filters={}, db_conn=get_collection('history'))
    return jsonify(response)


@app.route("/delete_log/<log_id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_log(log_id):
    if request.method == "DELETE":
        db = get_collection('history')
        db["history"].delete_one({"_id": ObjectId(log_id)})
        print("History deleted successfully!")
        return jsonify({"id": log_id, "message": "History deleted successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
