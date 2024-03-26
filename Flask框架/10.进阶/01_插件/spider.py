import requests


# res = requests.get('http://127.0.0.1:5000/')
# print(res.text)

for i in range(20):
    res = requests.get('http://127.0.0.1:5000/')
    print(res.text)