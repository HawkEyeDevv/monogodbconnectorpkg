import pandas as pd
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import json
import os

load_dotenv()
mongo_key = os.getenv("Mongodb_password")
"""
uri = f"mongodb+srv://Dracule:{mongo_key}@cluster0.xwl9vs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
"""

class Mongodbconnection:
    def __init__(self, client_url: str, database_name: str, collection_name: str):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_client(self):
        main_client = MongoClient(self.client_url)
        return main_client

    def create_database(self):
        db_client = self.create_client()
        database = db_client[self.database_name]
        return database

    def create_collection(self, collection_name=None):
        database = self.create_database()
        collection = database[collection_name]
        return collection

    def insert_record(self, record):
        collection = self.create_collection()
        if type(record) is list:
            for data in record:
                if type(data) is not dict:
                    raise TypeError("Type of the Data in record is not dict")
            collection.insert_many(record)
        elif type(record) is dict:
            collection.insert_one(record)

    def bulk_insert(self, file_path: str):

        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path, encoding="utf-8")
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)

        datajson = json.loads(data.to_json(orient="records"))
        collection = self.create_collection()
        collection.insert_many(datajson)

