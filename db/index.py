import requests 
url = "http://icanazdadjoke.com/"

response = requests.get(url, headers={ "Accept":"Application/json"})

data = response.json()

print(data["joke"])


 sqlite_version()
 
 #
 #
 #
 #
 