from fastapi import APIRouter
from typing import List, Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date


app03 = APIRouter()

class Addr(BaseModel):
    province: str
    city: str

class User(BaseModel):
    # name: str = Field(regex='^[a]') # regex参数被pattern参数替代
    # name: str = Field(pattern='^[a]')
    name: str
    age: int = Field(default=1, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

class Data(BaseModel):
    data: List[User]

@app03.post("/user")
async def user(user:User):
    print(user, type(user))
    print(user.name, user.birth)
    print(user.model_dump()) # dict()被model_dump()替代
    return user

@app03.post("/data")
async def data(data: Data):
    return data