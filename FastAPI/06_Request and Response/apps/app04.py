from fastapi import APIRouter, Form
from typing import List, Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

from starlette.datastructures import FormData

app04 = APIRouter()

@app04.post("/regin")
async def reg(username:str=Form(), password:str=Form()):
    print(f"username: {username} password: {password}")
    return {
        "username": username
    }
