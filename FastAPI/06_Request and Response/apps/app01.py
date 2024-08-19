from fastapi import APIRouter

app01 = APIRouter()

@app01.get('/user/1')
def get_user():
    return {"user_id": "root user"}

@app01.get('/user/{id}')
def get_user(id: int):
    # print("user_id", id, type(id))
    return {'user_id': id}

