from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index")
def index(request: Request):
    name = "root"
    age = 99
    books = ['红楼梦', '西游记', '三国演义', '水浒传']
    info = {"name": "Cai", "age": 24, "gender": "male"}
    return templates.TemplateResponse(
        "index.html", # 模板文件
        {
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "pai": 3.1415926
        }, # context上下文对象,一个字典
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)