from fastapi import APIRouter

from models.user import User
# from config.db import conn
from config.db import db  # Import db instead of conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId
user = APIRouter()


@user.get('/api')
async def find_all_users():
    return usersEntity(db["py_mongo_collection"].find())

@user.get('/api/{id}')
async def find_one_user(id):
    return userEntity(db["py_mongo_collection"].find_one({"_id": ObjectId(id)}))

@user.post('/api')
async def create_user(user:User):
    db["py_mongo_collection"].insert_one(dict(user))
    return usersEntity(db["py_mongo_collection"].find())

@user.delete('/api/{id}')
async def delete_user(id, user:User):
    return userEntity (db["py_mongo_collection"].delete_one({"_id":ObjectId(id)})) 

# @user.put('/api/{id}')
# async def update_user(id, user:User):
#     db["py_mongo_collection"].find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
#     return userEntity( db["py_mongo_collection"].find_one({"_id":ObjectId(id)}))

# Define route for updating a user
@user.put('/api/{id}')
async def update_user(id: str, user: User):
    # Retrieve existing user data from MongoDB
    existing_user = db["py_mongo_collection"].find_one({"_id": ObjectId(id)})
    if existing_user:
        # Create a dictionary containing only the fields that are not None in the request
        update_fields = {key: value for key, value in user.model_dump().items() if value is not None}
        # Update the user with the specified fields
        db["py_mongo_collection"].update_one({"_id": ObjectId(id)}, {"$set": update_fields})
        # Retrieve and return the updated user entity
        updated_user = db["py_mongo_collection"].find_one({"_id": ObjectId(id)})
        return updated_user
