from fastapi import FastAPI
import uvicorn
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04

app = FastAPI()

app.include_router(app01, tags=["01 路径参数"])
app.include_router(app02, tags=["02 查询参数"])
app.include_router(app03, tags=["03 请求体数据"])
app.include_router(app04, tags=["04 form表单数据"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)