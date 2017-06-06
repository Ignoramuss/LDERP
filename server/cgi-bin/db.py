#!/home/mayank/Envs/lderp/bin/python
from pymongo import MongoClient
from config import DB_URI, DB_NAME

def insert_in_collection(collection_name, document):
    mongodb_uri = DB_URI
    database_name = DB_NAME

    client = MongoClient(mongodb_uri)
    db = client[database_name]
    collection = db[collection_name]
    ack = collection.insert_one(document).acknowledged
    return ack
