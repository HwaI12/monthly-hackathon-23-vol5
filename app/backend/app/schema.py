from pydantic import BaseModel
from fastapi import Query
# Request Body
class UserRequest(BaseModel):
    name: str = Query(...,)
    password:str= Query(...,)
