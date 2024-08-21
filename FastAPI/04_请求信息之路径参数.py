from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    return {'user_id': user_id}

@app.get('/article/{article_id}')
async def get_article(article_id: int):
    return {'article_id': article_id}

@app.get("/user/me")
async def read_user_me():
    return {"username": "the current user"}

@app.get("/user/{username}")
async def read_user(username: str):
    return {"username": username}

if __name__ == '__main__':
    uvicorn.run("04_请求信息之路径参数:app",port=8080, reload=True)