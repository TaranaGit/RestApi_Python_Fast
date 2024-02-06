from pymongo import MongoClient
# Add the url of mongo db 
conn = MongoClient("Connection String") 
db = conn["test"]
collection = db["py_mongo_collection"]

