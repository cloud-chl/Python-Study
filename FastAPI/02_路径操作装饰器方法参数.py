from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
async def get_test():
    return {"method": "Get方法"}

@app.post('/post')
async def post_test():
    return {"method": 'Post方法'}

@app.put('/put')
async def put_test():
    return {"method": "Put方法"}

@app.delete('/delete')
async def delete_test():
    return {"method": "Delete方法"}

if __name__ == '__main__':
    uvicorn.run("02_路径操作装饰器方法参数:app", port=8000, reload=True)