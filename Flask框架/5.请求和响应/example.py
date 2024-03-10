import requests

# GET 请求
res = requests.get('http://127.0.0.1:5000/request/?name=lisi&age=33&name=Cai',
                   cookies = {'name': 'hello'})
print(res.text)

# POST请求
# res = requests.post('http://127.0.0.1:5000/request/', data={'name': 'Cai', 'age':24})
# print(res.text)