import requests

url = "https://{domain}.atlassian.net/rest/api/3/user/"
headers = {
  "Accept": "application/json;charset=UTF-8",
  "Authorization": "Basic {access token}"
}
users = {"603901787x3a4600x89x9085",
         "603901787x3a4600x89x9085",
         "603901787x3a4600x89x9085"}

for user in users:
  query = {'accountId': user}
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
  )
  data = response.json()
  #print(data)
  print("Felhasználó: "+data['displayName']+ ", " +data['emailAddress'])
  print(response.status_code)
