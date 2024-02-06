from pymongo.results import DeleteResult

def userEntity(item) -> dict:
    if isinstance(item, DeleteResult):
        return {"message": "User deleted successfully"}# Return a message indicating successful deletion
    else:
        return {
        "id": str(item["_id"]),
        "name": item.get("name", ""),
        "email": item.get("email", ""),
        "password": item.get("password", ""),
        "gender": item.get("gender", ""),  # Use get() to handle missing key
        "role": item.get("role", "")  
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity] 