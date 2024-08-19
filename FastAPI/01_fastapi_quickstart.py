from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
async def hello():
    return {'message': 'Hello, World!'}

@app.get('/shop')
async def fruit():
    return {'items': ['apple', 'banana', 'cherry']}

if __name__ == '__main__':
    uvicorn.run("fastapi_quickstart:app",port=8080, reload=True)