import urllib.request
import urllib.parse

data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
req = urllib.request.Request("https://www.example.com", data=data, method="post")
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
print(html)