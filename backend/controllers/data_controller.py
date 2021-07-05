import json
from bson import json_util, ObjectId


def add_light_controller(payload, db_conn):
    try:
        if not all(param in payload for param in ['light_name', 'light_state', 'light_color']):
            raise Exception("Parameter are missing to save light")
        print('--->')
        print(payload)
        result = db_conn["lights"].insert_one(payload)
        print(result.inserted_id)
        print(result.acknowledged)
        return {
            "success": True,
            "id": str(result.inserted_id),
            "message": "Lights created successfully",
        }

    except Exception as e:
        return {"success": False, "message": "Error in api: " + str(e)}


def add_thermostat_controller(payload, db_conn):
    try:
        if not all(param in payload for param in ['thermostat_name', 'temperature']):
            raise Exception("Parameter are missing to save thermostat")
        result = db_conn["thermostat"].insert_one(payload)
        print(result.inserted_id)
        print(result.acknowledged)
        return {
            "success": True,
            "id": str(result.inserted_id),
            "message": "Thermostat created successfully",
        }

    except Exception as e:
        return {"success": False, "message": "Error in api: " + str(e)}


def add_history_controller(payload, db_conn):
    try:
        print('Inside add_history_controller')
        print(payload)
        result = db_conn["history"].insert_one(payload)
        print(result.inserted_id)
        print(result.acknowledged)
        return {
            "success": True,
            "id": str(result.inserted_id),
            "message": "History created successfully",
        }

    except Exception as e:
        return {"success": False, "message": "Error in api: " + str(e)}


def all_lights_controller(filters, db_conn):
    print("from lights_list...")
    try:
        result = db_conn["lights"].find(filters).sort("created_on", -1)
        lights_list = []
        for d in result:
            lights_list.append(
                {
                    "id": str(d["_id"]),
                    "light_name": str(d["light_name"]),
                    "light_color": str(d["light_color"]),
                    "light_state": d["light_state"],
                    "created_on": d["created_on"].strftime("%b %d %Y %H:%M:%S"),
                }
            )
        return lights_list
    except Exception as e:
        print(e)
        return {"success": False, "message": "Error in api: " + str(e)}


def all_thermostat_controller(filters, db_conn):
    print("from lights_list...")
    try:
        result = db_conn["thermostat"].find(filters).sort("created_on", -1)
        thermostat_list = []
        for d in result:
            thermostat_list.append(
                {
                    "id": str(d["_id"]),
                    "thermostat_name": str(d["thermostat_name"]),
                    "temperature": str(d["temperature"]),
                    "created_on": d["created_on"].strftime("%b %d %Y %H:%M:%S"),
                }
            )
        return thermostat_list
    except Exception as e:
        print(e)
        return {"success": False, "message": "Error in api: " + str(e)}


def get_existing_state(name, filters, db_conn):
    if name == 'lights':
        result = db_conn['lights'].find_one(filters)
        state = "ON" if result['light_state'] else "OFF"
        return {'id': str(result['_id']), 'state': state}
    else:
        result = db_conn['thermostat'].find_one(filters)
        temperature = result['temperature']
        return {'id': str(result['_id']), 'temperature': temperature}


def all_history_controller(filters, db_conn):
    print("from lights_list...")
    try:
        result = db_conn["history"].find(filters).sort("created_on", -1)
        history_list = []
        for d in result:
            history_list.append(
                {
                    "id": str(d["_id"]),
                    "applianceType": str(d["appliance_type"]),
                    "eventType": str(d["event_type"]),
                    "description": d["event_description"],
                    "applianceName": d["appliance_name"] if 'appliance_name' in d else '',
                    "createdOn": str(d["created_on"]),
                }
            )
        return history_list
    except Exception as e:
        print(e)
        return {"success": False, "message": "Error in api: " + str(e)}
