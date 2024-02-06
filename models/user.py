from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List
      
class User(BaseModel):
    name: str
    email: str
    password: str
    gender:str
    role :str 
    
    