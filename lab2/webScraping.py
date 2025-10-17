import requests

#url = "https://www.example.com"
# this will get all the HTML, javascript, css code
#response = requests.get(url)
from bs4 import BeautifulSoup

url = "https://www.youtube.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(title, content, links)