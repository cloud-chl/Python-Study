from fastapi import APIRouter, Request
from pydantic import BaseModel, EmailStr
from typing import Union

app07 = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

@app07.post("/user")
async def create_user(user: UserIn):

    return user