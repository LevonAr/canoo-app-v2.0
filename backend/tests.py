import unittest
from bson import json_util, ObjectId

import controllers.data_controller as models
from database import get_collection


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Setting up test variable")

        """" Test cases with different parameters for testing each module used in app function """
        cls.valid_light_data = dict(light_name="testlight", light_color="red", light_state=False)
        cls.empty_light_data = dict()
        cls.missing_value_in_lights = dict(light_name="testlight", light_color="red")
        cls.valid_thermo_data = dict(thermostat_name="testthermo",temperature="40 F")
        cls.invalid_thermo_data = dict()

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nTesting Completed")

    def test_insert_lights(self):
        result = models.add_light_controller(payload=self.valid_light_data, db_conn=get_collection('lights'))
        self.assertTrue(len(result['id']) == 24)
        db = get_collection('lights')
        db["lights"].delete_one({"_id": ObjectId(result['id'])})

    def test_with_empty_insertion(self):
        result = models.add_light_controller(payload=self.empty_light_data, db_conn=get_collection('lights'))
        self.assertTrue('Parameter are missing to save light' in str(result['message']))

        result = models.add_thermostat_controller(payload=self.empty_light_data, db_conn=get_collection('thermostat'))
        self.assertTrue('Parameter are missing to save thermostat' in str(result['message']))

    def test_with_missing_value_insertion(self):
        result= models.add_light_controller(payload=self.missing_value_in_lights, db_conn=get_collection('lights'))
        self.assertTrue('Parameter are missing to save light' in str(result['message']))

        result= models.add_thermostat_controller(payload=self.missing_value_in_lights, db_conn=get_collection('thermostat'))
        self.assertTrue('Parameter are missing to save thermostat' in str(result['message']))


    def test_insert_thermostat(self):
        result = models.add_thermostat_controller(payload=self.valid_thermo_data, db_conn=get_collection('thermostat'))
        self.assertTrue(len(result['id']) == 24)
        db = get_collection('thermostat')
        db["thermostat"].delete_one({"_id": ObjectId(result['id'])})






if __name__ == '__main__':
    unittest.main()
