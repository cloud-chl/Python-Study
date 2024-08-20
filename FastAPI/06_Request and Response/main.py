from fastapi import FastAPI
import uvicorn
from apps.app01 import app01
from apps.app02 import app02

app = FastAPI()

app.include_router(app01, tags=["01 路径参数"])
app.include_router(app02, tags=["02 路径参数"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)