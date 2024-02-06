from pymongo import MongoClient
# Add the url of mongo db 
conn = MongoClient("mongodb+srv://Tarana:1234@nodetuts.dejcbjk.mongodb.net/") 
db = conn["test"]
collection = db["py_mongo_collection"]

