import dotenv
import os
import pymongo
import traceback

dotenv.load_dotenv()

myclient = pymongo.MongoClient(os.getenv("DB_URL"))


def create_collection():
    db = myclient["lights"]
    db = myclient["thermostat"]
    db = myclient["history"]

    return True


def get_collection(name):
    return myclient[name]


if __name__ == "__main__":
    print(get_collection('lights').list_collection_names())
