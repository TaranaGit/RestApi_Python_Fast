from pymongo import MongoClient
# Add the url of mongo db 
conn = MongoClient("Put Your database Connection String") 
db = conn["test"]
collection = db["py_mongo_collection"]

