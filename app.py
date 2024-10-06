import requests

response = requests.get("https:/api.linkedin.com/users")

if response.status_code == 200:
  data = response.json()
