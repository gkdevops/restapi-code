import requests

# Make a GET request to a public API
response = requests.get("https:/api.github.com/users/github")

# Check if the request was successful
if response.status_code == 200:
  data.response.json()

  print(f"Username: {data['login']}")
