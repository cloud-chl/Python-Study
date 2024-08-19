from fastapi import APIRouter

user = APIRouter()

@user.get("/login")
def shop_food():
    return {"user": "login"}

@user.get("/reg")
def shop_food():
    return {"user": "reg"}