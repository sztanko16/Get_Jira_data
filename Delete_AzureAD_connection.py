import requests

link = "https://api.atlassian.com/scim/directory/{tenant}/Users/"
user = {"38e92xb3-2856-45d0-bx69-72e9x4d12ae9",
        "e0fdcx13-0364-4396-ax6b-e00cx89581a4"}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {access token}"
}

for item in user:
    apiUrl = link+item
    response = requests.delete(
    apiUrl,
    headers=headers
  )
    data = response.json()
    print(data['detail'])
    print(response.status_code)
