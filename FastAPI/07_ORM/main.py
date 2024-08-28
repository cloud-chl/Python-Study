from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app = app,
    config = TORTOISE_ORM,
)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)