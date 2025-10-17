import requests

data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)

