import requests
URL = input("Enter URL: ")
r = requests.get(url=URL)
data = r.cookies
print(data)