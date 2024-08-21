from fastapi import APIRouter, Request

app06 = APIRouter()

@app06.post("/items")
async def items(request: Request):
    print("URL:", request.url)
    print("客户端IP地址:", request.client.host)
    print("客户端宿主:", request.headers.get("User-Agent"))
    print("cookies", request.cookies)
    return {
        "URL": request.url,
        "客户端IP地址:": request.client.host,
        "客户端宿主:": request.headers.get("User-Agent"),
        "cookies": request.cookies,
    }