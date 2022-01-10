from pymongo import MongoClient
from bson import ObjectId
import requests
import sys
import json


class Service:

    @staticmethod
    def login(username,email):
        # --------- Remove----------
        username = 'Bret'
        email = 'Sincere@april.biz'
        # --------- Remove----------
        resp = requests.get('https://jsonplaceholder.typicode.com/users')
        users = resp.json()
        user = list(filter(lambda user : user["username"] == username and user["email"] == email,users))
        if len(user) > 0:
            return True
        return False
    
    @staticmethod
    def save_file(file_name,data):
        with open(sys.path[0] + f"/{file_name}.json","w") as f:
            json.dump(data, f)
    
    @staticmethod
    def load_file(file_name):
        with open(sys.path[0] + f"/{file_name}.json","r") as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def load_from_DB():
        client = MongoClient(port=27017)
        db = client["LibraryDB"]
        library_collection = db["Library"]
        data = library_collection.find_one(
            {"_id":ObjectId("61dc08fd81b6fb3b29226524")})
        return data


