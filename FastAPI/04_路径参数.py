from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items",tags=['这是一个items测试接口'],
         summary="this is items测试 summary",
         description="this is items测试 description...",
         response_description="this is items测试 response_description...",
         deprecated=True,
         )

def test():
    return {"items": "items 数据"}


if __name__ == '__main__':
    uvicorn.run("03_路径操作装饰器方法的参数:app", port=8000, reload=True)