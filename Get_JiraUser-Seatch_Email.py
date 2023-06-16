import requests

url = "https://{domain}.atlassian.net/rest/api/3/user/search"

headers = {
  "Accept": "application/json;charset=UTF-8",
  "Authorization": "Basic {access token}"
}
user = {"user@domain.com",
        "user@domain.com"}

for item in user:
  query = {'query': item}
  response = requests.request(
     "GET",
    url,
    headers=headers,
    params=query
  )

  data = response.json()
  if not data:
    print("Nincs adat")
  else:  
    print(data[0]['accountId'])
