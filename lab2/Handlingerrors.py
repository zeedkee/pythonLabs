import requests

#       here we use an endpoint that always gives a 404 status error
#response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
#if response.status_code != 200:
 #   print(f"HTTP Error: {response.status_code}")



#            Setting a Timeout
# url = "https://httpbin.org/delay/10"

#try:
#    response = requests.get(url, timeout=5)
#except requests.exceptions.Timeout as err:
#    print(err)

#             HTTP Request Headers
auth_token = "XXXXXXXX"

# here we set the authorization header with the 'bearer token' for authentication purposes.
headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())