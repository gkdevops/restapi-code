import requests

response = requests.get("https:/api.github.com/users/github")

if response.status_code == 200:
  data = response.json()
