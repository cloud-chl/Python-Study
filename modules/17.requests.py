import requests

url = 'http://www.baidu.com'
# response = requests.get(url)

# str类型
# print(response.text)

# bytes类型，可以进行decode操作
# print(response.content.decode())

# 手动设定编码格式
# response.encoding = 'utf-8'

# 常见的响应对象参数和方法
# 响应url
# print(response.url)

# 状态码
# print(response.status_code)

# 响应对应的请求头
# print(response.request.headers)
# 响应头
# print(response.headers)

# 响应的对应请求的cookie
# print(response.resquest.cookies)
# 响应的cookie
# print(response.cookies)

# 自动将json字符串类型的响应内容转换为python对象（dict or list）
# print(response.json())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
# 发送带请求头的请求
response2 = requests.get(url, headers=headers)
print(response2.content.decode())

