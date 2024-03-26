import requests

# res = requests.get('http://127.0.0.1:5000/hello/')
# res = requests.post('http://127.0.0.1:5000/hello/')
# res = requests.put('http://127.0.0.1:5000/hello/')
# res = requests.delete('http://127.0.0.1:5000/hello/')
res = requests.get('http://127.0.0.1:5000/user4/',
                   json={'name': 'Cai', 'age': 24},
                   headers={'Content-Type': 'application/json',
                            'Cookie': 'key=6AD525768103295411C2E182D1A65DE2'})
print(res.text)
